## Cloning the GitHub repository

Assuming you already have Git [installed](https://git-scm.com/download/), anybody can clone this repository by following these steps:

1. Open the command prompt/terminal on your machine;
2. Type the command 'cd' followed by the directory you wish to store the repository in;
3. Go to the top of the [GitHub repository](https://github.com/kiehozero/pintbaby/) and click the green 'Code' drop-down button;
4. Copy the [link provided](https://github.com/kiehozero/pintbaby.git);
5. Return to the Command Prompt and type 'git clone' followed by the copied address.

For an in-depth guide to cloning repositories, click [here](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/), from which the steps above were taken.

## Django
>>> Installation information, creation of databases, runserver, makemigrations, etc.

## Heroku

I deployed this project to Heroku using the following method:

1. After setting up a [Heroku](https://www.heroku.com/) account and creating a new app, head back to your terminal and set up a requirements.txt file that automatically updates when you import a library. Instead of using the regular 'touch' command, enter 'pip3 freeze -- local > requirements.txt' into the terminal and press enter;
2. Run the 'python app.py > Procfile' command to create a file that Heroku will use to run your app automatically, as opposed to you using the python3 app.py command each time you open Gitpod;
3. Push both the Procfile and requirements.txt to your repository;
4. In the Heroku app settings, click the Connect to GitHub button and select the repository you wish for Heroku to connect to. Click the Config Variables button and select the Reveal option, and enter the items that were added to your env.py file line-by-line. Since you added it to .gitignore, Heroku will not be able to see it in the GitHub
repository.
5. Once the connection is confirmed, scroll down to the bottom and click the Enable Automatic Deployment button.
6. After a couple of minutes select the Open App button, and you will now have a hosted URL for the project. Unlike Gitpod or any other IDE, this app will only update when you push changes to your repository.

## Amazon Web Services

>>> S3 - Quick storage setup for media and static files

>>> IAM - Lock up your S3 bucket by using the IAM console to control access and security

## Python Libraries

This project is built on the [Django](https://www.djangoproject.com/) framework. A number of libraries were installed to complete this project, and can be installed simply by using the pip3 install command in the command line interface.

- [django-allauth](https://pypi.org/project/django-allauth/) is an authentication and account management library;
- [dj_database_url](https://pypi.org/project/dj-database-url/) - quick access to configure a database to your local environment;
- [gunicorn](https://pypi.org/project/gunicorn/) - a HTTP server dyno to power Heroku apps;
- [stripe](https://stripe.com/docs/api?lang=python/) - Stripe's official API;
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - take the hassle out of form alignment and design with crispy-forms.
- [boto3](https://pypi.org/project/boto3/) - A Python software development kit for Amazon Web Services
- [django-storages](https://pypi.org/project/django-storages/) - To quote the PyPI directory, "a project to provide a variety of storage backends in a single library."
- [pylint-django](https://pypi.org/project/pylint-django/) (if you install it)