# Heroes_vs_Villains

Project setup:

1. create virtual enviroment.
    pipenv install

2. access shell
    pipenv shell

3. set python interpreter.
    pipenv --venv
    copy path
    ctrl + p 
    search Python select interpreter
    past path into "Enter interpreter path"


Install pipenv install:
     Django
     mysqlclient
     djangorestframework

1. pipenv install django

2. install mysqlconnector or mysqlclient (they work the same)
    pipenv install mysqlclient

3. install RESTframework
    pipenv install djangorestframework

once this is pushed to github. if it's cloned down all installed packages will 
automatically be installed.


CREATING NEW PROJECT

1. django-admin startproject <project name> .

        a space and . is needed after the project name 
        so that the files can be placed in the name of 
        the project folder.

        it's good practice to use project as the end
        of your projcet name so to not confuse files. 


Link Project to mysqlclient

1. create a local_settings.py file in the project folder.

2. in settings.py scroll to databases. 
    cut the entire section out and past it into local.settings.py
    This new file is already marked in gitignore so whatever 
    is in that file will not be pushed. 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql", *** make sure ENGINE is changed from sqlite to mysql
        "NAME": "cars_database",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "password"

    }
}

3. at the bottom of our setting.py file 

try:
    from cars_project.local_settings import *
except ImportError:
    pass

4. CUT out the SECURYT KEY from settings.py and past into local_settings.py. 

git commits will not have user info and secret keys. 
    

App creation:
        python manage.py startapp <app_name>

            1. create serializer file in new app
            2. create urls file
            3. add app to installed apps
                project folder > installed apps > add app to list


Register APP
    1. go to created app admin file
    2. from .models import <app_name>

    3. reigister model
        admin.site.register(<app_name>)


Serialize APP  
    ~ helps convert JSON into pyhton objects and python objects into JSON

1. in app folder create file serializer.py

    import. 
    from rest_framework import serializers

2. import app. 
    from .models import <app_name>

3. in serializers file - create class.
 ~ the class is always named after the model followed by Serializer 

    class CarSerializer(serializers.ModelSerializer): 
        class Meta:
            model = Book
            fields = ["type"]


Connect applictaion to mysql workbench
    1. +sql
    
    2. CREATE DATABASE <database_name> *must be name of the databse created
       in the settings files. (now found in local_settings.py)

    3. lightning bolt 

    4. refresh
    
    5. database shold be seen under schemas. 

    6. python manage.py migrate (defined table shold be created)


Make Migrations, Migrate, and push to github
    1. python manage.py makemigrations <app_name> optional
    2. python manage.py migrate
    3. push to github


Linking Apps with Foreigh Key




