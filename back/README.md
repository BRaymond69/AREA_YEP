## Run the API

- Create and use a python virtual environment at the root of the repository
```pip install virtualenv; virtualenv .venv; source .venv/bin/activate```



- Install all dependencies
```pip install -r requirement.txt```

- Creat Database
```./manage.py migrate```
```./manage.py migrate --run-syncdb```

- Migrate Cron
```python3 manage.py migrate django_cron ```

- Run the API server
```python3 manage.py runserver```

## Use the API

server running on http://127.0.0.1:8000/

You can directly connect with the API with your web browser for testing purposes.

available endpoints :
- register/
- login/
- checkserver/

You can find automated tests for endpoints in authApp/tests.py
If you want to see the results of the tests, uncomment the 'print' functions in tests.py
To run the tests : run the API on a terminal, and on a second terminal execute :
python3 manage.py test

## Endpoints and how to use them

### Authentication
#### register/

| ![POST](https://i.imgur.com/jiDbJMf.png) | register/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'username': '...',
    'email': '...',
    'password': '...'
}
        
```
Data received:
        
```yaml
{
  'data': {
      'email': '...',
      'id': ..., # ne vous sers à rien
      'username': '...'
  }
}
        
```
</details>

#### login/

| ![POST](https://i.imgur.com/jiDbJMf.png) | login/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'username': '...',
    'password': '...',
}
        
```
Data received:
        
```yaml
{
    'Authorization': 'Token ...'
}
        
```
</details>

#### logout/

| ![POST](https://i.imgur.com/jiDbJMf.png) | logout/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
}
        
```
Data received:
        
```yaml
{
    'data': 'You logged out successfully'
}
        
```
</details>

<<<<<<< HEAD
* services/
You SEND to the API: [GET]
{
    'token': '...',
}

You RECEIVE:
{
    'data': {
        'configured': [
            ...
        ]
        'unconfigured': [
            ...
        ]
    }
}

* facebook/
You SEND to the API: [POST]
### Services

#### facebook/

| ![POST](https://i.imgur.com/jiDbJMf.png) | facebook/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'password': '...', <--- if it is first time connecting, you can change password and email by re-sending them.
    'email': '...' <--- if it is first time connecting
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### intra/

| ![POST](https://i.imgur.com/jiDbJMf.png) | intra/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'autoToken': '...' <--- Autologin link
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### twitch/

| ![POST](https://i.imgur.com/jiDbJMf.png) | twitch/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'twitchAccount': '...' <--- Account Twitch who are in live
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### twitter/

| ![POST](https://i.imgur.com/jiDbJMf.png) | twitter/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'twitterAccount': '...' <--- Name of Twitter Account
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### mail/

| ![POST](https://i.imgur.com/jiDbJMf.png) | mail/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'email': '...' <--- email address
    'password' : '...' <--- Password Email address
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### news/

| ![POST](https://i.imgur.com/jiDbJMf.png) | news/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'newsPapper': '...' <--- A Subject of your choise (ex: Tesla, Coronavirus, Skate, ...)
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### film/

| ![POST](https://i.imgur.com/jiDbJMf.png) | film/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'FilmNumber': '...' <--- Number of film upper than 0
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### netflix/

| ![POST](https://i.imgur.com/jiDbJMf.png) | netflix/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'NetflixNumber': '...' <--- Number of in coming Netflixfilm upper than 0
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### amazon/

| ![POST](https://i.imgur.com/jiDbJMf.png) | amazon/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'AmazonNumber': '...' <--- Number of in coming Amazonfilm upper than 0
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

#### date/

| ![POST](https://i.imgur.com/jiDbJMf.png) | date/
|---|---|
<details> <summary>Details</summary>
Data to be sent:
    
```yaml
{
    'Authorization': 'Token ...',
    'DayName': '...' <--- a day of the week in english with uppercase at beginning of the day
}
        
```
Data received:
        
```yaml
{
    'data': '...'
}
        
```
</details>

* Mail/
You SEND to the API: [POST]
{
    'Authorization': 'Token ...',
    'email': '...' <--- email address
    'password' : '...' <--- Password Email address
    'subject' : <-- Subject of email
}

