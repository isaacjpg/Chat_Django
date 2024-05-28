# Django Chat Application

This is a Django Chat projecto to demostrate the user of websockets protocols, Redis for websockets and cache, and postgresql for user management. 

The applications includes a signup and login pages and creates a room everytime it ecounters a new pair of users to chat. The messages are stored in a Redis chache so it can be fetch everytime the user joins the conversation. 
## Installation Virtual Env

1. Create a python's virtual enviroment

```bash
  python3 -m venv venv
```
2. Install requirements.txt
```bash
  pip install requirements.txt
```
if you encounter problems installing uWSGI, remove it from requirements.txt

3. Set the enviroment variables in a .env file in root level with the followin variables. 
```bash
    DOCKERIZED=False
    SECRET_KEY=your-secret-key
    DEBUG=True (enabling Django DEBUG)
    DATABASE_DB= (your postgres database name)
    DJANGO_SETTINGS_MODULE=core.settings 
    DATABASE_HOST=(your postgres database host)
    DATABASE_PORT=(your postgres database port)
    DATABASE_USER=(your postgres database user)
    DATABASE_PASSWORD=(your postgres database password)
    REDIS_HOST=(your redis host)
    REDIS_PORT=(your redis password)
```

4. Run the django start command
 ```bash
  python manage.py runserver
```

## Installation using Docker 

Yo can run the whole package runing docker-compose. Just need to set a .env file with 
```bash
    DOCKERIZED=True
```
The package contains postgress, redis and nginx services for sync and async servers. 

## Usage
Access the root url. If you are not logged in, it will redirect to the login page, you can go to sign up to create a new user and then login. 

After login in you will encounter a list of registered users. Just click the user you want to chat with. It is not necesary that the other user is online to write. All messages will be in cache and can be read when the other user connects. 

To go back to the list of users, just click GOBACK and to log out click LOG Out. 

## Logs
You can find logs in the logfiles folder.
