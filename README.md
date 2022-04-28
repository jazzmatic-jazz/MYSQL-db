SIMPLE SAMPLE PROJECT USING MySQL DATABASE.

1. Installing Mysql to the system.
2. Creating a Database in MySQL Command Line:
    CREATE DATABASE <name>
3. Creating user:
    CREATE USER '<USER>'@'<localhost>' IDENTIFIED WITH mysql_native_password BY '<PASSWORD>';
4. Granting access:
    GRANT ALL ON <DATABASE>.* TO '<USER>'@'localhost';
5. Flush the privileges so that the current instance of MySQL knows about the recent changes you’ve made:
    FLUSH PRIVILEGES;
6. Install the mysqlclient:
    pip install mysqlclient
7. Fill in the details accordingly:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}

8. USE <database>;
9. SHOW TABLES;