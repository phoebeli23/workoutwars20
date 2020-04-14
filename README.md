# Workout Wars 2020
Pie Queens workout wars application

## Getting Started

### Fork and Clone the Git Repository
1. Make sure you are signed into github and have git installed on your computer.
2. In the top right corner of this page, click `Fork`. This will create your own copy of the codebase on your account. Feel free to rename the app from `workoutwars20` to fit the year.
3. From your newly forked repository on Github, click `Clone or Download` and copy the http url. Then, from your terminal, navigate to where you'd like to store the workout wars files and run the following command:
```
git clone [YOUR-REPO-URL]
```
For example, I would have run `git clone https://github.com/cidneyweng/workoutwars20.git`.

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
4. Navigate into your cloned repository (make sure you use the name of your repo if you changed it from `workoutwars20`):
```
cd workoutwars20
```
5. Now we need to create the environment to hold our requirements.
```
virtualenv -p /usr/local/bin/python3 pqenv
```
The `-p` flag tells `virtualenv` the path to the python version you want to use. If yours is different, make sure to replace it. The name `pqenv` is the environment name.

6. You should now have a folder called `pqenv` inside your `workoutwars20` folder. Your structure should now look something like this:
```
workoutwars20
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
1. Make a copy of `settings-example.py` (in `workoutwars20/workoutwars/workoutwars`) in the same directory and title it `settings.py`.
2. Open `settings.py` and make sure that `DEBUG` is set to `True`.
3. Change the `SECRET_KEY` to a long, random string of characters. This is for security reasons.
4. Navigate to the app root (`workoutwars20/workoutwars`) and prepare your models for the database:
```
python manage.py makemigrations
```
5. Set up the database by loading the model files into sqlite:
```
python manage.py migrate
```
6. Now, you can launch the application!
```
python manage.py runserver
```
If run succesfully, you will be given an IP address in the command line, which when copied into your browser, should display the workout wars home page.

## Deploying the Application
So far you've launched the app locally and learned how to import data. But how do you make it accessible to everyone else? These instructions are for hosting on a linode server, but feel free to use a different server if you are familiar with any.

### Setting up the Server
1. Follow Linode's [Getting Started Guide](https://linode.com/docs/getting-started/) to set up the server. A few things to note:
  - You will have to create an account and put in billing information. Don't worry - your treasurer will reimburse you for the cost of the server. There are also many promo codes out there for new accounts so get yourself some free credit!
  - The 2GB Linode with 50GB of storage is more than enough for us.
  - **IMPORTANT**: Make sure you select **Ubuntu 16.04** as your OS - this will be important later.
  - You can choose your hostname to be whatever you want. I named mine `piequeens`
  - When updating /etc/hosts, you can use `workoutwars.piequeens.org` as your FQDN. Make sure to add both the IPv4 and IPv6 lines to the file. For example:
  ```
  127.0.0.1       localhost
  127.0.1.1       ubuntu.members.linode.com       ubuntu
  45.33.49.32     workoutwars.piequeens.org       piequeens
  2600:3c01::f03c:91ff:fe71:182d  workoutwars.piequeens.org       piequeens
  ```
2. While you are ssh'd into root on the server, we are going to add a limited user account called `pqadmin`
```
adduser pqadmin
```
Make sure you remember this password! You can store it in the secret google doc for safekeeping.

3. We will give this user admin privileges by running this command:
```
adduser pqadmin sudo
```
4. We also need to add the user to the `www-data` group:
```
adduser pqadmin www-data
```
5. If you are interested, it would be worth your time to look into the guide to [secure your server](https://linode.com/docs/security/securing-your-server/), but you can come back to that later.

### Linking the Domain Name
Next you need to set up workoutwars.piequeens.org to point to your new server. Follow these steps to do that:

1. Log onto [www.godaddy.com](www.godaddy.com) using the pie queens username and password (can be found on the workout wars google doc which is not linked here for security reasons).
2. Under `Domains`, next to `piequeens.org`, select `DNS`.
3. Find the record named `workoutwars` of type `A` and edit the IP to point to the public **IPv4** address of your new server.
4. Find the record named `workoutwars` of type `AAAA` and edit the IP to point to the public **IPv6** address of your new server.  Make sure to save your changes.

### Set up your Environment on Ubuntu 16.04
1. Now that the server and domain are ready to be used, we can ssh into our new user with our new domain. To exit out of the root account, press CTRL+D. Then ssh back in with the new account:
```
ssh pqadmin@workoutwars.piequeens.org
```
2. Install the system packages required for nginx, the SQLite Python bindings, and managing Python Tools:
```
sudo apt-get update
sudo apt-get install nginx python3-dev python3-pip
((((sudo apt-get install build-essential nginx python-dev python3-pip python-sqlite sqlite git))))
```
3. Install `virtualenv` and `virtualenvwrapper`:
```
sudo -H pip3 install virtualenv virtualenvwrapper
```
4. For `virtualenvwrapper` to function correctly, run the following commands:
```
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
```
5. Activate virtualenvwrapper in the current session:
```
source ~/.bashrc
```
6. Install uWSGI using pip:
```
sudo pip3 install uwsgi
```
7. Be sure that you’re in the `pqadmin` user’s home directory and create the virtual environment for the application:
```
cd /home/pqadmin && mkvirtualenv pqenv
```
After executing this command your prompt will change to something like ``(pqenv)pqadmin@piequeens~$`` indicating that you are using the sample virtual environment.

8. Install your dependencies:
```
pip install django
pip install django-bootstrap4
```
9. Clone your forked github repository:
```
git clone [your repo http url].git
```
10. Make a copy of `settings-example.py` called `settings.py`:
```
cp /home/pqadmin/workoutwars20/workoutwars/workoutwars/settings-example.py /home/pqadmin/workoutwars20/workoutwars/workoutwars/settings.py
```
11. Open `settings.py`:
```
nano /home/pqadmin/workoutwars20/workoutwars/workoutwars/settings.py
```
Change the secret key to a long, random string of characters. Make sure to keep this a secret!
```python
SECRET_KEY = `very long string of random characters`
```
Change the debug attribute to false:
```python
DEBUG = False
```
Change the ALLOWED_HOSTS IP to the IP of your server:
```python
ALLOWED_HOSTS = ['workoutwars.piequeens.org', [YOUR SERVER IP], '127.0.0.1']
```
Don't forget to save your changes!

12. Check to see if the server is set up correctly by launching the application in developer mode (remember to replace `workoutwars20` with your repo name if you changed it):
```
cd workoutwars20/workoutwars
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```
Navigate to [workoutwars.piequeens.org:8080](workoutwars.piequeens.org:8080) in your browser. The workout wars app should show up. Don't worry if it doesn't look styled correctly. We'll get to that in a bit. When you're done testing this, take it down by pressing `CTRL+C` in the terminal.

### Configure uWSGI
uWSGI is an application server that can communicate with applications over a standard interface called WSGI.
1. Quickly test the application server by passing the information for our app:
```
uwsgi --http :8080 --home /home/pqadmin/Env/pqenv --chdir /home/pqadmin/workoutwars20/workoutwars -w workoutwars.wsgi
```
If you go to [workoutwars.piequeens.org:8080](workoutwars.piequeens.org:8080), you should see the app again. When you're done testing this, take it down by pressing `CTRL+C` in the terminal.

2. Now that you know that uWSGI works from the command line, we'll create configuration files for it to manage your app automatically. First create a directory to store these files:
```
sudo mkdir -p /etc/uwsgi/sites
```
3. Create and open a file for workout wars:
```
sudo nano /etc/uwsgi/sites/workoutwars.ini
```
4. Paste the following into the file and save it (remember to replace `workoutwars20` with your repo name):

```
[uwsgi]
project = workoutwars
uid = pqadmin
projenv = pqenv
base = /home/%(uid)

chdir = %(base)/workoutwars20/%(project)
home = %(base)/Env/%(projenv)
module = %(project).wsgi:application

master = true
processes = 5

socket = /run/uwsgi/%(project).sock
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true
```
5.  Create an systemd unit file to manage the uWSGI emperor process and automatically start uWSGI at boot:
```
sudo nano /etc/systemd/system/uwsgi.service
```
6. Paste the following contents in it and save:

```
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown pqadmin:www-data /run/uwsgi'
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```
7. Start the `uwsgi` service:
```
sudo systemctl start uwsgi
```

### Configure nginx
We will be using nginx as our reverse proxy.
1. Remove the default nginx site configuration if there is one:
```
sudo rm /etc/nginx/sites-enabled/default
```
2. Create a server block configuration file for our project:
```
sudo nano /etc/nginx/sites-available/workoutwars
```
3. Inside, paste the following (remember to replace `workoutwars20` with your repo name):
```
server {
    listen 80;
    server_name workoutwars.piequeens.org;

    location = /favicon.ico {access_log off; log_not_found off; }
    location /static/ {
        root /home/pqadmin/workoutwars20/workoutwars;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/workoutwars.sock;
    }
}
```
4. Create a symlink to nginx’s `sites-enabled` directory to enable your site configuration file:
```
sudo ln -s /etc/nginx/sites-available/workoutwars /etc/nginx/sites-enabled
```
5. Check nginx’s configuration and restart it:
```
sudo nginx -t
sudo systemctl restart nginx
```
6. Allow uWSGI and nginx to start automatically at boot:
```
sudo systemctl enable nginx
sudo systemctl enable uwsgi
```
7. You should now be able to reach workout wars at [workoutwars.piequeens.org](workoutwars.piequeens.org)!

### Useful Links
- We roughly followed [Digital Ocean's django deployment guide](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04) to deploy workout wars. If anything doesn't make sense, this is a great place to start. It has more in-depth explanations about what each step is actually doing. If you get confused, this is a great resource! The troubleshooting section at the bottom is especially useful **if you're having trouble configuring uWSGI and/or nginx**. 

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

## Managing the Application
To get workout wars ready for everyone to start logging, you will need to do a few things.
1. Load class, exercise, and team data into the app by following the instructions below.
2. create a superuser so you can give yourself admin privileges
```
python manage.py createsuperuser
```
3. Now you can navigate to [workoutwars.piequeens.org/admin](workoutwars.piequeens.org/admin) and log in with the superuser you created to add, delete, or modify any data in the app.
4. Eventually, once you have your workout-logging account created, you'll be able to give yourself admin privileges. While logged into the admin dashboard as your superuser, select `Users`, and then your username. Under `Permissions`, check the boxes for "Staff status" and "Superuser status". This will allow you to control the application without having to log off of your personal account. If you do this, you can delete the superuser you originally created so it doesn't affect your scoreboards.
5. You're going to need to update the year in a couple places in the app. Open up `workoutwarsapp/forms.py` and change the date selection dates to the correct years.
```python
widget=forms.SelectDateWidget(years=(2017, 2018),
        months={12:('December'), 1:('January')}),
```
Next, open up `workoutwarsapp/views.py` and change the start date to the correct start date for this year.
```python
START_DATE = datetime.date(2017, 12, 18)
```
You might want to read through the home page as well and update it to match your description for this year by making changes in `workoutwarsapp/templates/index.html`.
6. This one is more for captains than for you, but for people to be able to begin using the site, they are going to need to know which team they are on so they can pick it when they sign up. The teams should be sent out before people start signing up.

### Making Changes to the Code
We strongly recommend that you make all your changes locally on your computer, and merely pull them from github on the server. For the server to reflect changes you've made:
1. Activate the virtual environment
```
workon pqenv
```
2. Navigate to your repository and pull changes:
```
cd /home/pqadmin/workoutwars20
git pull origin master
```
3. Let uWSGI and nginx know that the files have been updated:
```
sudo touch /etc/uwsgi/sites/workoutwars.ini
```
4. You should now see your changes reflected in production!


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
2. Place these csv files into the `fixtures` folder (inside `workoutwars20/workoutwars`)
3. Make sure your virtual environment is active (instructions listed above, if necessary)
4. Install simplejson:
```
pip3 install simplejson
```
5. `cd` into the `fixtures` folder and create json files by running:
```
python csv2json.py teams.csv workoutwarsapp.team
python csv2json.py classes.csv workoutwarsapp.class
python csv2json.py exercises.csv workoutwarsapp.exercise
```
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
Repeat for classes and exercises:
```
python manage.py loaddata classes.json
python manage.py loaddata exercises.json
```
