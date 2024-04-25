# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
import accounts.models as models
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    form = UserChangeForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined', 'is_mapped', 'unique_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'unique_id')

    readonly_fields = ('unique_id',)  # Add this line to make unique_id non-editable


    def change_password(self, request, id, form_url=''):
        if request.method == 'POST':
            user = self.get_object(request, id)
            form = self.form(user, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['password1']
                if user.check_password(new_password):
                    messages.error(request, "You have already used this password. Please choose a different one.")
                    return self.response_change(request, user)
                user.set_password(new_password)
                user.save()
                return self.response_change(request, user)
        else:
            form = self.form(user)
        return self.render_change_form(request, context={'form': form, 'change': True, 'is_popup': "_popup" in request.POST, 'save_as': False, 'has_delete_permission': False, 'has_change_permission': True, 'has_absolute_url': False, 'opts': self.model._meta, 'original': user}, form_url=form_url, add=True)


class UserBasicDetailsAdmin(admin.ModelAdmin):

    list_display = ('id','user','gender','date_of_birth','profile_image','phone_number','company','data_sources_json',)
    list_filter = ('user','date_of_birth','id','gender','profile_image','phone_number','company','data_sources_json',)


class UserActivityAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'activity_type', 'timestamp')
    list_filter = ('user', 'timestamp', 'id', 'activity_type')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.User, UserAdmin)
_register(models.UserBasicDetails, UserBasicDetailsAdmin)
_register(models.UserActivity, UserActivityAdmin)
