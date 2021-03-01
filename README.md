# Portfolio Website
Django version of my personal porftfolio website.

# Get Started
- Install python on your machine.
- (Optional): Install django in a virtual environment:
  - ### How to install virtualenv
      #### Install pip first
      ``` sudo apt-get install python3-pip ```
      #### Install virtualenv using pip3
      ``` sudo pip3 install virtualenv ```
      #### Create a virtual environment
      ``` virtualenv <virtual_environment_name> ```
      ### Active your visual environment
      ``` source <virtual_environment_name>/bin/activate ```
  - ### How to install django
      ### With virtual environment active install django
     ``` pip install django ```
     
 - clone repository
 - run django app
    ``` python manage.py runserver ```
 - Go to http://localhost:8000

# HTML Pages
All html pages are in the pages/templates/pages.

# Static Files (CSS, Javascript)
/pages/static/pages

# Project Directory

```bash
.
├── .gitignore
├── README.md
├── manage.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   └── pages
│   │       ├── css
│   │       │   ├── images
│   │       │   │   └── banner.jpg
│   │       │   └── style.css
│   │       ├── images
│   │       │   ├── banner.jpg
│   │       │   └── profile-1.jpeg
│   │       └── js
│   │           └── script.js
│   ├── templates
│   │   └── pages
│   │       ├── about.html
│   │       └── base.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── personal_portfolio
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
 ```
