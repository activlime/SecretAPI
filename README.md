# SecretAPI

* API where you keep your sects using django
* For accounts, you must go through a browser
* I chose html because I can validate the data quickly, it is user friendly, and common
* valid users are confirmed using user_id and token authentication to verify if valid user
* I use that id to grab secrets that belong to the user
* I chose to use django because it handles a lot of the database attributes for me


NOTE**All responses are in ```json```

## Next steps
1. More tests with requests to make sure no breaks
2. change framework to django rest framework because it is a lot simpler and cleaner; didn't use because not much documention
3. create more error checks for user errors

## tests
1. unit tests included
2. postman inputs off all requests
3. postman wrong inputs all requests
4. postman request to access or delete not allowed secret

## Installation
1. ```sudo apt-get install python-pip```
2. ```sudo pip install virtualenv```
2. ```sudo apt-get install python3-dev libpq-dev```
3. ```mkdir django```
4. ```cd django```
5. ```virtual env -p [python 3 path] venv```
6. ```source venv/bin/activate```
7. ```pip install django```
8. ```pip install psycopg2```
9. ```git clone [repo]```
10. ```sudo apt-get install postgresql```
11. ```python manage.py syncdb```
12. optional: deployment environment add secrests.middlewares.SSLMiddleware in settings.py
12. ```python manage.py runserver```

## Usage
* all post, get, delete requests require user and token verification
* to start server ```python manage.py runserver```


#### html to create account
```
POST /secrets/accounts/
```
* create user in form

#### get token
```
POST /secrets/token/new.json
```
* params = {"username" : [username], "password" : [password]}
* example response: ```{"success": true, "token": "2uy-420a8efff7f882afc20d", "user": 1}```

#### get all secrets created by user
```
GET /secrets/?user=[user_id]&token=[token]
```

#### post secret 
```
POST /secrets/?user=[user_id]&token=[token]
```
*params = {"description" : [description]}

#### get secret through secret_id
```
GET /secrets/[secret_id]/?user=[user_id]&token=[token]
```

#### update secret through secret_id
```
POST /secrets/[secret_id]/?user=[user_id]&token=[token]
```
*params = {"description" : [description]}

#### get secret through secret_id
```
DELETE /secrets/[secret_id]/?user=[user_id]&token=[token]
```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

jpulgarin for the tokens
