## Table of contents

* [Car rental website](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Domain Description](#domain_description)
* [License](#license)

## Car rental website

There is a website for car rental company (non-commercial)

## Screenshots

Plans: include logo/demo screenshots etc.\

## Technologies

HTML, CSS, Python 3.7.1, framework Django 2.2.5, Database Sqlite and so on...\
Supporting Programs: Sublime Text 3 - editor with a free evaluation period,
PyCharm - is an integrated development environment (IDE) used in computer programming, specifically for the Python language 

## Setup
> The instructions for starting a web site locally on a computer are described for users Linux and OS X

First of all to create and run all the web applications that we will develop throughout, you will need working copies 
of the following software:
*	[The Python Programming Language](https://www.python.org/downloads/)
*	[virtualenv: A tool to create isolated environments for Python packages](https://virtualenv.pypa.io/en/latest/installation.html)
*	[pip: The package manager to install Python packages](https://pip.pypa.io/en/stable/installing/)

You need to find a directory in which you want to create the virtualenv on yours PC.\
I have created a virtualenv called myvenv. The general command is in the format:

```
$ python3 -m venv myvenv
```

Start your virtual environment by running:

```
$ source myvenv/bin/activate
```

After all these steps you need to run Car_rental-website project, install it locally using clone command in terminal or
under the repository name, click Clone or download.
This command copies all the files in a repository to your computer,
and begins tracking them in git. You do this by typing in on the command line:
 
```
$ git clone https://github.com/RadchenkoVlada/Car_rental-website.git
```
 
Now that you have your virtualenv started, you can install Django.
Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

```
$ python -m pip install --upgrade pip
```
Now, run pip install -r requirements.txt to install Django.

```
(myvenv) ~$ pip install -r requirements.txt
Collecting Django~=2.2.4 (from -r requirements.txt (line 1))
  Downloading Django-2.2.5-py3-none-any.whl (7.1MB)
Installing collected packages: Django
Successfully installed Django-2.2.5
```

That's it! You're now ready to use a Django application! 


**Starting the web server**

You need to be in the directory that contains the manage.py file (in the directory where you have loaded project). 
In the console, we can start the web server by running python manage.py runserver:

```
(myvenv) ~/your_directory$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 24, 2019 - 23:46:36
Django version 2.2.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now you need to check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or 
whatever you use) and enter this address:

```
http://127.0.0.1:8000/
```

Congratulations! You've just launched my first website using a web server! Isn't that awesome?

## Domain Description

My task is to track the financial performance of the rental. There are a number of **cars** of various brands in your 
fleet, which are additionally stored data such as
* car name
* cost
* photo
* number of passengers
* cost
* year of manufacture 
* type
* brand
* availability of air conditioning or not
* availability of automatic transmission or not


Each car has its own rental cost.

**Customers** apply to the rental center. All customers are required to register, in which standard information 
* last name 
* first name
* username
* email address
* password

is collected about them.\
In the future, these users will be able revisiting the site using their unique username and password through "Sign in" page.\
But on the other hand, you can be a guest and first pick up a car for yourself, and then register.
\
All quoted rates are fully cancellable before 48 hours before pick up the car.

When a car is issued a **contract** is concluded. Each contract includes the 
* contract number
* the date of issue
* the expected date of return

The cost of car rental should depend not only on the car itself, but also on the period of its rental.

After the expiration of the rental contract, the client is obliged to return the car in proper form. When the car is returned in an improper form, the client pays a fixed set of fines (a single penalty for damage to property and the cost of repairing the car).

## License
[MIT](https://choosealicense.com/licenses/mit/)

------------------------
