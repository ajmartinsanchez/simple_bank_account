# simple_bank_account V2

# Docker function
In this first version we have working a docker enviroment. We have three principal commands for work with docker:

1.- docker-compose build will build all project, I recommend use it when some requirements.txt has been changed.
2.- docker-compose up will start server.

3.- docker-machine ip will be used only if you try to access to localhost:port and nothing is found, this command will show ip which are listening.

If you need launch some manage.py command, you can use next code, but always with a docker-compose up launched

docker-compose exec web python manage.py [command]

Example:
    docker-compose exec web python manage.py migrate

More information in https://docs.docker.com/compose/django/#create-a-django-project

# oAuth enviroment

For work with google oAuth, we need make a little hack.

First, we need to see what ip we have assigned.
Second, with this ip we need to go https://console.developers.google.com, active Google+ API, with all this, go to credentials and create a new one, and it's important redirect to http://IP.nip.io:8002/account/complete/google-oauth2/.
Third, put your credentials in settings.


# Steps for start to use this code.

1.- Our first step is run the proyect, we have an docker enviroment with posgresql database. You can follow the steps for docker that i explaine before, if you have some doubt please let me know.
2.- With out docker enviroment launched, we need follow steps explaine in Oauth eviroment.
3.- Once you have everything configured, you need create a super user with command:
    docker-compose exec web python manage.py createsuperuser

    This command will create a super user, you can try a login with gmail and then give to created user a staff permission, then you can have a correct login.

4.- Now you only need test it everything.