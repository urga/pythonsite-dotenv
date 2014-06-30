#Pythonsite-dotenv

Is a single python module that is intended to serve as a dependancy of a python project that needs to run in a
virtual environment. It configures the python interpreter so that a .env file is red which expands the environment with
security-sensitive settings.
I came up with the idea to try to get a consistent workflow for a django project when either developing or running in
production.


##What I tried before:
- Using virtualenwrapper and it's hooks, but I wanted to avoid using virtualenvwrapper on the production server.
- Patching manage.py to read the environment (using django-dotenv), but then gunicorn wouldn't load the environment


##My use case:
I use pythonsite-dotenv as a dependancy of the Django applications I develop (or any wsgi application for that matter),
so my workflow becomes:
1) Initialize a virtual environment (using virtualenv, virtualenvwrapper or pyvenv, it shouldn't matter)
2) pip install -r requirements.txt (which install this package)
3) create or edit a .env file where sensitive info is stored (SECRET_KEY, DATABASE_URL, ...)
4) run manage.py, gunicorn or any other python executable and it automatically has the expected environmnetal variables
defined.

This works either on a local development machine or on a shared host. Running the application becomes a matter of
pointing to the right executable, which means I can easily have multiple python applications running on a shared host:

<PATH_TO_MY_VIRTUALENV>/bin/gunicorn

If using supervisord or something else, I don't have to define environmental variables again. And when deploying, I can
simply change the environment by editing the .env file.


##How it works:
It simply places a sitecustomize module in the current python environment which reads the .env file that has to be
located at the root of the virtual environment.