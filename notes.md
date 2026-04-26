# Web Application Framework: DJango

#### Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.It follows the model-template-view (MTV) architectural pattern and provides a robust set of tools for building web applications.

## Create a Django project:

```
django-admin startproject blogproject
```
- This will create a project stucture something like:
``` 
blogproject/
    manage.py
    blogproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

## Create a Django app:
```
    python manage.py startapp blog
```
provide the app structure of this command: python manage.py startapp blog 
```
    blog/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    migrations/
        __init__.py
```

---

## define views in views.py:

```python
from django.shortcuts import render
from django.http import HttpResponse
#dummy data for testing
posts = [
    {
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'author': 'John Doe',
        'date_posted': 'June 1, 2024'
    },
    {
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'author': 'Jane Smith',
        'date_posted': 'June 2, 2024'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

---

## Database in Django

Django uses:
SQLite (default)
✔ Already configured
✔ No installation needed

- settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
- 'db.sqlite3' - This file will be auto-created after migrations are run. It will contain the database for your project.

### Define models in models.py:

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
## how many different datatypes are there in the above model?
- there are 4 different datatypes in the above model:
1. CharField: used for the title and author fields, which are short text fields.
2. TextField: used for the content field, which is a longer text field.
3. DateTimeField: used for the date_posted field, which stores date and time information.
4. AutoField: used for the id field, which is an automatically generated primary key for each post (not explicitly defined in the model but automatically added by Django).

### Migrations:
- Migrations are a way to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They are like version control for your database schema. When you make changes to your models, you create a migration file that describes those changes, and then you apply the migration to update the database schema accordingly.
- To create a migration after defining your model, you run:
```python manage.py makemigrations
```
- To apply the migration to the database, you run:
```python manage.py migrate
```
- This will create the necessary tables in the database based on your model definitions.

---

## Admin Panel
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
The above code registers the `Post` model with the Django admin site. 
By doing this, you can manage the `Post` model through the Django admin interface. 
This means you can create, read, update, and delete instances of the `Post` model directly from the admin dashboard without needing to write any additional code for handling these operations.

## where to find this admin interface?
- You can access the Django admin interface by running your development server and navigating to 
- `http://localhost:8000/admin/` in your web browser.
- You will need to create a superuser account to log in to the admin interface. 
- You can create a superuser by running the following command in your terminal:
```python manage.py createsuperuser
``` 
- Follow the prompts to enter a username, email, and password for the superuser account.
- Once you have created the superuser account, you can log in to the admin interface using
- the credentials you just created.
- After logging in, you will see the `Post` model listed under the "Blog" section (or whatever you named your app). 
- You can click on the `Post` model to view, add, edit, or delete posts through the admin interface.


---

## Registering the app:
- After creating your app, you need to register it in your project's settings.py file:
```python
INSTALLED_APPS = [
    # other apps
    'blog.apps.BlogConfig',
]
```
'blog.apps.BlogConfig'- is the path to the app's configuration class, 
which is defined in the `apps.py` file of your app. 
This tells Django to include your app in the project and 
allows you to use its features, such as models, views, and templates.

---

## Defining templates:
- In your Django app, you typically create a `templates` directory to store your HTML templates. 
- Inside the `templates` directory, you can create a subdirectory with the same name as your app (e.g., `blog`) to organize your templates. 
- For example, you would create the following directory structure:
```blogproject/
    blog/
        templates/
            blog/
                base.html
                home.html
                about.html
```
- In your views, you can then render these templates by specifying the path to the template file. For example, in the `home` view, you would use:
```pythonreturn render(request, 'blog/home.html', context)
```
- This tells Django to look for the `home.html` template in the `blog/templates/blog/` directory.

## base.html:
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
<!--Navbar-->
{% block content %}{% endblock %}
<!--Sidebar-->
```

## home.html:
```html
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <article class="media content-section">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="#">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}
{% endblock content %}
```

---

## defining url patterns:

-- In your project's `urls.py` file, you include the URL patterns from your app. 
- For example, in the `blogproject/urls.py` file, you would have:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

- In your app's `urls.py` file, you define URL patterns that map to your views. 
- For example, in the `blog/urls.py` file, you might have the following URL patterns:
```python
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='blog-home'),
    path('about/',views.about, name='blog-about'),
]
```

---

## To run the development server, use the following command:
```python manage.py runserver
```
- This will start the Django development server, and you can access your application at `http://localhost:8000/` in your web browser. 
- You should see the home page of your blog application, and you can navigate to the about page by going to `http://localhost:8000/about/`. 
- You can also access the admin interface at `http://localhost:8000/admin/` to manage your posts and other models.


---

# Designing a RESTful Web API:

- REST (Representational State Transfer) is an architectural style for designing networked applications.
- A RESTful API is an API that adheres to the principles of REST.
- RESTful APIs use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources.
- Resources are identified by URLs (Uniform Resource Locators).
- RESTful APIs are stateless, meaning that each request from a client to the server must contain all the information needed to understand and process the request.
- RESTful APIs can return data in various formats, such as JSON (JavaScript Object Notation) or XML (eXtensible Markup Language).
- RESTful APIs are widely used in web development to enable communication between different systems and applications. 
- They allow developers to create scalable and flexible APIs that can be easily consumed by client.


- To create a RESTful API in Django, you can use the Django REST framework, which provides a powerful and flexible toolkit for building Web APIs.
- djangorestframework is a third-party package that you can install using pip:
```
pip install djangorestframework
```
Add to settings.py:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

