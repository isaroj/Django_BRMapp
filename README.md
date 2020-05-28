# Django_BRMapp
## Table of contents
* [General info](#General_info)
* [Technologies](#Technologies)
* [set up](#set_up)

## General info
This is a book-record-management application, where a new user can sign up or a existing user can log in to the BRMapp.
In this app a user can get various functionalities sucha as add book, edit book, delete book, view books, search book.
The BRMapp stores various data about a book i.e. book name, author name, publisher name, price etc.

## Technologies
Python V 3.6.5  is used as the backend programming language.
HTML5 and CSS3 are used for front end development.
SQLite3 is used for database purpose.
DJango 3.0.6 is used as framwwork to develop this application.

## set up
Use command django -admin startproject projectname.
Now make a pull request to download the entire BRMapp and place the entire folder under your project folder.
Move the static folder outside the BRMapp folder.
Now we have to some changes in settings.py module.
Register the BRM app in INSTALLED_APPS list in settings.py .
Now to set path for the static files use the following command in settings.py module.
STATIC_DIR=os.path.join(BASE_DIR,'static')
Now set the path for the static folder by adding following lines
STATIC_URL = '/static/'
STATICFILES_DIRS=[
   STATIC_DIR,
]
To configure SQLite3 with Django write the following
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
Now we have to set urls for project level by writing following lines
path('BRMapp/',include("BRMapp.urls"))
write the above line in urlpatterns list of outer folder not the BRMapp level urls.
Now we will set the application level urls by creating urls.py file in BRMapp and adding the paths in BRMapp level urls.py (Refer urls.py module of BRMapp)
At this point first generate sql statemets by using python manage.py makemigrations command.
Now to execute these sql commands so that a DB will be created use python manage.py migrate
To start the server use command python manage.py runserver
Now give the urls in the address bar to execute the BRMapp subsequently.



