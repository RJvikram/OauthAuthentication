# OauthAuthentication
OauthAuthentication

## Setting up PostgreSQL Credentials
To set up PostgreSQL credentials for your application, follow these steps:

1. **Create User with that password:**
   ```bash
   CREATE USER oauthUser WITH PASSWORD 'AuthUser!1234';
This command creates a user named oauthUser with the specified password.

2. **Create Database with all create, update, and delete permissions:**
First, connect to your PostgreSQL server using a client like psql or a GUI tool like pgAdmin.
    ```bash
    psql -U postgres -h localhost -p 5432 ```

Then, execute the following SQL commands to create the database and grant permissions:
    ```bash
    CREATE DATABASE OauthAuthentication;
    GRANT ALL PRIVILEGES ON DATABASE OauthAuthentication TO oauthUser;

Make sure to replace localhost:5432 with the actual hostname and port of your PostgreSQL server if it's hosted elsewhere.

This markdown snippet can be included in your repository's README file, providing clear instructions for setting up PostgreSQL credentials for your application.
