# Django Rest Framework Minimal Starter

Look at the [Django Rest Framework](https://www.django-rest-framework.org/#quickstart) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# Creating the virtual environment
py -m venv venv

# Activating the virtual environment
.\venv\Scripts\activate

# Installing dependencies
pip install -r ./requirements.txt
```

## Development Server

Start the development server on `http://127.0.0.1:8000/`:

```bash
# Running the server
py .\manage.py runserver
```

## Migrations

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

```bash
# Creating new migrations based on the changes you have made to your models.
py .\manage.py makemigrations

# Applying and unapplying migrations.
py .\manage.py migrate
```

Check out the [Django Documentation](https://docs.djangoproject.com/en/5.0/) and [Rest Framework Documentation](https://www.django-rest-framework.org/) for more information.