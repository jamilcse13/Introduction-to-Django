# Django:
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design
- Django is based on MVT (Model-View-Template) architecture.

## Start a django project
- go to the targetted directory and run: 
    - django-admin startproject djangoProject
- go to the project directory and run:
    - python3 manage.py startapp djangoApp
- we can create multiple app inside out project
- run the project on server:
    - python3 manage.py runserver

## Virtual Environment
- Install virtual environment golabally
    - pip install virtualenv
- Then create my own virtual environment in my project
    - virtualenv venv
- Then again install django in virtual env (inside the project)
- Start with virtual env: . venv/bin/activate
- store the requierments packages with version within the project by this command:
    - pip freeze > requirements.txt
- Then when someone work with this project, he just need to run the command for installing these pacages:
    - pip install -r requirements.txt

# Ptoject Setup
- djangoProject->settings.py: include the app name 'djangoApp' inside INSTALLED_APPS
- djangoProject->urls.py: include the apps urls 'path('', include('djangoApp.urls'))' inside urlpatterns
- create urls.py inside djangoApp

# MVT:
- M for Model: by which we can connect database.
- V for Views: where we write the business logics
- T for Template: this is the frontend part

# Template:
- extends: we can extend parent page into another (child) page by using this in the child page
    - {% extends template_file_name %}
- block-endblock: we can change a specific portion from parent page to child page. This should write both parent and child page
    - {% block title %}Modified Title{% endblock %}
    - {% block content %}Modified Content{% endblock %}
