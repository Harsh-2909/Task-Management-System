# Task Management System

A task management app for Projects created using Django v4.0 and Python 3.8 for educational purpose. This project was created during a One Day Hackathon on 11th December 2021.

<!-- ## Demostration

**CREATING A TASK**

![Creating a Post](http://g.recordit.co/Pn4287QG2G.gif)

**UPDATING AND DELETING A TASK**

![Updating and Deleting a Task](http://g.recordit.co/YK6qBdFYNQ.gif)

**ACCOUNT CREATION AND SIGN IN**

![Account Creation and Login](http://g.recordit.co/i5jpi0HkyE.gif) -->

## How to Setup in Localhost

1. Clone this repository.
2. Open the cloned repository.
3. Install dependencies using ``pip install -r requirements.txt``
**OR**
Install ``pipenv`` using ``pip install pipenv`` and initialise a Virtual Machine using ``pipenv install`` in the directory.
4. Set environment variables like `SECRET_KEY`, `DEBUG_VALUE`, etc, using the `python-decouple` library and creating a `.env` file in your main directory. An example file isprovided.
5. Run the Django Server using ``python manage.py runserver`` and then goto ``localhost:8000`` or ``127.0.0.1:8000`` and see the server running.

### Environment Variables:

`SECRET_KEY`: Django secret key which can be any long hexadecimal value. Django recommends *atleast* **50 characters** to make it secure. Use the below code for generating new keys.
```python3.8
import secrets

print(secrets.token_urlsafe())
```
`DEBUG_VALUE`: Set it as **"True"** for Debug environment and **"False"** for Production.
`EMAIL_USER`: The email address that will be used to email incase somebody forgets password.
`EMAIL_PASS`: The password to that email address. Refer to [App Passwords](https://myaccount.google.com/apppasswords) if the email has 2 factor auth.

## How to Setup for Production

Refer on how to deploy Python apps in Heroku [here](https://devcenter.heroku.com/articles/deploying-python) and Django app configuration [here](https://devcenter.heroku.com/articles/django-app-configuration).

## Features

- Can create any tasks and assign it to somebody.
- Can keep track of the status of the task.
- Password can be recovered using the password recovery features.
- Profile System with a profile image.
- Follows most of the Django security checks.
- Uses Django Class Views for handling Projects and Tasks.

#### Known Issues:

- App not ready for production due to bucket issues as it can't handle profile pictures or any other attacments.

*Please make a GitHub issue if any other bugs are found.*

## Notes

This project was created on **Ubuntu-20.04 LTS** and tested under **Windows 10** and **Ubuntu**, and is expected to work fully in other systems too.

This project is still under development. Parts of the source codes may not be well documented. Also suitable prompts may not be available for the user at the moment.

More features and fixes are yet to come. Meanwhile suggestions, ideas, bug reports are welcomed.