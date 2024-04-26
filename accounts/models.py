from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.dispatch import receiver
from django.db import models
import uuid
# Create your models here.
def get_current_datetime():
    return timezone.now()

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(('email address'), unique=True)
    join_date = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def get_full_name(self):
        """Returns the full name of the user if both first name and last name exist."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return ""

    def get_short_name(self):
        """Returns the short name of the user if both first name and last name exist."""
        if self.first_name and self.last_name:
            return f"{self.first_name[0]}{self.last_name[0]}"
        else:
            return ""
    
    def __str__(self):
        return self.email
        

    class Meta:
        db_table = "User"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class UserBasicDetails(models.Model):
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Unsure', 'Unsure',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userBasicDetails")
    gender = models.CharField(max_length=6, choices=SEX_CHOICES, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=False, blank=False, default=get_current_datetime)
    profile_image = models.ImageField(upload_to="user_profile", blank=True, null=True, default="user_profile/user_icon.png")
    phone_number = models.CharField(max_length=14, null=True, blank=True)

    class Meta:
        db_table = "UserBasicDetails"
    
    def image_tag(self):
        if self.profile_image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.profile_image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userActivityLog")
    activity_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create User Token created behalf of each and every user as well as UserBasicDetails
@receiver(post_save, sender=User)
def create_auth_token(instance=None, created=False, **kwargs):
    """ create user token """
    if created:
        Token.objects.create(user=instance)
        UserBasicDetails.objects.create(user=instance)


