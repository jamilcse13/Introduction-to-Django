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
- store the requierments packages with version within the project by this command:
    - pip freeze > requirements.txt
- Then when someone work with this project, he just need to run the command for installing these pacages:
    - pip install -r requirements.txt