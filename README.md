#Pythonsite-dotenv

Is a single python module that is intended to serve as a dependancy of a python project that needs to run in a
virtual environment. It configures the python interpreter so that a .env file is red which expands the environment with
security-sensitive settings.
I came up with the idea to try to get a consistent workflow for a django project when either developing or running in
production.

##What I tried before:
- Using virtualenwrapper and it's hooks, but I wanted to avoid using virtualenvwrapper on the production server.
- Patching manage.py to read the environment (using django-dotenv), but then gunicorn wouldn't load the environment
