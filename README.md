# SecretAPI

API where you keep your sects

NOTE**All responses are in ```json```

## Installation

1. install ```django```
2. install ```postgresql```
3. install ```django-tokenapi```

## Usage
* all post, get, delete requests require user and token verification


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
GET /secrets/[secret_id]?user=[user_id]&token=[token]
```

#### update secret through secret_id
```
POST /secrets/[secret_id]?user=[user_id]&token=[token]
```
*params = {"description" : [description]}

#### get secret through secret_id
```
DELETE /secrets/[secret_id]?user=[user_id]&token=[token]
```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

jpulgarin for the tokens
