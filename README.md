# Django-Project-Starter-Template
"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

A Django Template for creating basic webapp with basic features such as Authentication System, User Profile, etc.
The Template can be used out of the box for any type of website/webapp
<h1> Screen Shots </h1>
<font align="center">
<ul>
  <img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/index.png" alt=""/>
  <br><img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/Login_without_social_button.png"/>
  <img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/login_with_social_button.png"/>
  <img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/Signup.png"/>
  <br><img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/home.png"/>
  <br><img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/profile.png"/>
  <br><img src="https://raw.githubusercontent.com/mymi14s/mymi14s.github.io/master/admin.png"/>
</ul>
</font>

<h1>Language Requirement</h1>
  - Python 3.6 (Minimum >= 3.5)
  - Django 2.1.4 (Minimum >= 2.0)

<h1>Features</h1>

+ Authentication System (Using Django Allauth)
  - Login and Registration
  - Social Auth
  - Email Activation, Revocvery
  - Password Change, Reset

+ Profile System
  - Custom User Model
  - User Management and Profile
  - Edit User Profile

+ Bootstrap 4 Template System
  - Landing Page
  - Authentication
  - Dashboard
  - Global System Setting (Site name, site title, site email, site address, etc)

+ Email System
  - Email SMTP

+ Database System
  - MariaDb and MySQL
  - SQLite

+ Customizable
  - Built for easy modification and custom editing

<h1>How to Use</h1>
+ Install Python3 and Virtual Environment
  - Install Python3 from <a href="https://www.python.org">Python Software Foundation</a>
  - Create Virtual Environment
    - $ mkdir django-starter && cd django-starter
    - $ python3 -m venv myenv && source myenv/bin/activate

+ Pull source from github
  - $ git clone https://github.com/mymi14s/Django-Project-Starter-Template.git
  - $ cd Django-Project-Starter-Template/src
  - $ pip install -r requirements.txt

+ Create SECRET_KEY and SUPERUSER
  - Generate SECRET_KEY at <a href="https://www.miniwebtool.com/django-secret-key-generator/">miniwebtool</a>
  - Edit core/settings.py line 36
    - Change SECRET_KEY = '<font color="red">9ea*4cwjzn@e9-qhsmkj^%94$8e$=0rgb@%6ort#9(sacs15ui</font>' to new KEY
  - Create SUPERUSER
    - $ python manage.py createsuperuser
    - $ python manage.py runserver
    - Open 127.0.0.1:8000 and login

+ OPTIONAL CONFIGURATION
  - EMAIL Settings
    - Open core/settings.py and edit with your detail on line 198 to 202

      - EMAIL_USE_TLS = True
      - EMAIL_HOST = 'Your SMTP'
      - EMAIL_HOST_USER = 'YOUR EMAIL'
      - EMAIL_HOST_PASSWORD = 'YOUR PASSWORD'
      - EMAIL_PORT = 587

  - MYSQL Configuration requires Mysqlclient
  - Visit <a href="https://pypi.org/project/mysqlclient/">Mysql Client</a>
  - Use the instruction provided.
  - Edit core/settings with your mysql database info.

+ CREDITS
  - <a href="https://github.com/pratikborsadiya/vali-admin">Pratik Borsadiya<a/>
  - <a href="https://colorlib.com/demo?theme=creative-agency">ColorLib</a>
