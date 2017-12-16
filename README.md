# Workout Wars 2017-2018
Pie Queens workout wars application

## Getting Started
### Fork and Clone the Git Repository
_insert instructions for forking/cloning git repo here_

### Setting Up Your Environment
_insert instructions for setting up environment here_

### Launching Application Locally
Launching the app locally is very simple. You simply need to prepare a few things before the app will run for the first time.
1. Prepare your models for the database by running the command: `python manage.py makemigrations`
2. Set up the database by loading the model files into sqlite using `python manage.py migrate`
3. Now, you can launch your application by running `python manage.py runserver`. If run succesfully, you will be given an IP address in the command line, which when copied into your browser, should display the workout wars home page.

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
3. Activate your virtual environment (instructions listed above, if necessary)
4. Install simplejson by running `conda install simplejson`
5. `cd` into the `fixtures` folder and create json files by running `python csv2json teams.csv workoutwarsapp.team`. Repeat for `class` and `exercise`
6. `cd` back into the `workoutwars` folder (run `cd ..`)
7. load data by running `python manage.py loaddata teams.json` (repeating for classes & exercises). You should see `Installed xx object(s) from 1 fixture(s)`

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
