# Workout Wars 2017-2018
Pie Queens workout wars application

## Getting Started

### Fork and Clone the Git Repository
1. Make sure you are signed into github and have git installed on your computer.
2. In the top right corner of this page, click `Fork`. This will create your own copy of the codebase on your account. Feel free to rename the app from `workoutwars18` to fit the year.
3. From your newly forked repository on Github, click `Clone or Download` and copy the http url. Then, from your terminal, navigate to where you'd like to store the workout wars files and run the following command:
```
git clone [YOUR-REPO-URL]
```
For example, I would have run `git clone https://github.com/fabiola17lopez/workoutwars18.git`.
4. You should now have the workout wars codebase downloaded on your computer. 
4. NOTE: only one person needs to fork the repository. Anyone else wanting to work on the application can be added as a collaborator on the repo. To add collaborators, select `Settings`>`Collaborators`. They will be able to clone and push updates to the forked repo.

### Setting Up Your Environment
1. If you don't have it already, download the latest version of `Python3` from the [python website](www.python.org). Unfortunately, Django does not support `Python2`. If you are on OSX and you have Homebrew installed you can do:
```
brew install python3
```
2. To verify that you have `Python3` set up correctly, open a terminal and type:
```
python3
```
You should see something like this:
```
Python 3.7.1 (default, Nov 28 2018, 11:51:54) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
This is the interactive Python shell. Hit `CTRL + D` or type `exit()` to exit it.
3. To avoid polluting our global scope with unnecessary packages, we are going to use a virtual environment to store our packages. One excellent virtual environment manager available for free is `virtualenv`. To install it:
```
pip3 install virtualenv
```
4. Navigate into your cloned repository (make sure you use the name of your repo if you changed it from `workoutwars18`):
```
cd workoutwars18
```
5. Now we need to create the environment to hold our requirements.
```
virtualenv -p /usr/local/bin/python3 pqenv
```
The `-p` flag tells `virtualenv` the path to the python version you want to use. If yours is different, make sure to replace it. The name `pqenv` is the environment name.
6. You should now have a folder called `pqenv` inside your `workoutwars18` folder. Your structure should now look something like this:
```
workoutwars18
├── pqenv
├── workoutwars
├── .gitignore
├── README.md
└── requirements.txt
```
7. You can now activate the environment:
```
source pqenv/bin/activate
```
You will see that the next line prompt begins with the environment name. That means the environment is active.
```
(pqenv)
```
8. Our application is written in Django, a framework for creating web applications in python. Install Django:
```
pip3 install django
```
9. For styling, we are using bootstrap. Install bootstrap:
```
pip3 install django-bootstrap4
```
10. That's it! Now you are ready to launch workout wars.

### Launching Application Locally
Launching the app locally is very simple. You simply need to prepare a few things before the app will run for the first time.
1. Prepare your models for the database:
```
python manage.py makemigrations
```
2. Set up the database by loading the model files into sqlite:
```
python manage.py migrate
```
3. Now, you can launch the application! 
```
python manage.py runserver
```
If run succesfully, you will be given an IP address in the command line, which when copied into your browser, should display the workout wars home page.

### Loading Data Into Application
Django makes loading initial data into an application very simple. Because players will create their own accounts and log their own workouts, the only data you need initially will be the team names, class names, and exercise details. In order to do this, we will be using Django fixtures.

Teams

ID | name
--- | ---
1 | Team 1 Name
2 | Team 2 Name

Classes

ID | name | plural
--- | --- | ---
1 | Freshman | Freshmen
2 | Sophomore | Sophomores

Exercises

ID | description | notes | increment | measurement | multiplier
--- | --- | --- | --- | --- | ---
1 | downhill skiing | enter time on mountain only | 15 | mins | 1.25

1. Create a csv file with the correct headers for each of the 3 tables. The structure is shown above. Save these as `teams.csv`, `classes.csv`, and `exercises.csv` respectively.
2. Place these csv files into the `fixtures` folder (inside `workoutwarsapp`)
3. Make sure your virtual environment is active (instructions listed above, if necessary)
4. Install simplejson:
```
pip3 install simplejson
```
5. `cd` into the `fixtures` folder and create json files by running:
```
python csv2json.py teams.csv workoutwarsapp.team
``` 
Repeat for `class` and `exercise`.
6. `cd` back into the `workoutwars` folder:
```
cd ..
```
7. Load the data:
```
python manage.py loaddata teams.json
```
You should see:
```
Installed xx object(s) from 1 fixture(s)
```
Repeat for classes and exercises.

### Deploying Application
_insert instructions for deploying application here_

## Understanding How the Application Works

### Database Structure
This app uses sqlite3 as its database, with 5 simple tables.
- `Users` - contains user authentication data (`first_name`, `last_name`, `email`, `password`)
- `Profile` - contains workout wars user data (`nick_name`, `team`, `class`)
- `Team` - contains team names for the 2-team split (`name`)
- `Class` - contains names of player classes (`name`, `plural`)
- `Exercise` - contains data for each type of exercise players can do (`description`, `notes`, `increment`, `measurement`, `multiplier`)
- `Workout` - contains data for workouts players have completed (`workout_date`, `user`, `exercise`, `duration`, `with_other_class`, `score`)

### Document Structure

When you look into the `workoutwars` folder, you will find a series of files and directories that are used by django to create and run your application. Below is a diagram of your document structure.

```
workoutwars
├── workoutwars -- main project folder
│        ├── __init__.py
│        ├── settings.py -- project settings
│        ├── urls.py -- project url routes
│        └── wsgi.py
├── workoutwarsapp
│        ├── migrations -- directory used by django to preserve data during database updates
│        └── static -- directory used to store static files
│        ├── templates -- directory that stores our HTML templates
│        ├── __init__.py
│        ├── admin.py
│        ├── apps.py
│        └── forms.py
│        ├── models.py
│        ├── tests.py
│        ├── urls.py -- app url routes
│        └── views.py
└── manage.py
```

### Django Basiccs
_insert basic django explanation here (e.g. views, models, etc.)_
