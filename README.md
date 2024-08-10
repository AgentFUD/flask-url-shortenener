# url-shortener-demo
A Simple URL Shortener written in Flask with SQLAlchemy

## How to run the demo ##

clone the repo

```bash
bash$ git clone git@github.com:AgentFUD/flask-url-shortenener.git
```

Create a virtual environment and activate it
```bash
bash$ python3 -m venv env
bash$ source env/bin/activate
```

Install dependencies
```bash
bash$ pip3 install -r requirements.txt
```

Run the app
```bash
bash$ flask run
```

Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Debug ##
You can check the database content with the sqlite3 command line tool

```bash
bash$ sqlite3 short_urls.sqlite 
SQLite version 3.40.1 2022-12-28 14:03:47
Enter ".help" for usage hints.
sqlite> select * from urls;
1|OooQWA|https://www.metzdowd.com/pipermail/cryptography/2023-March/038128.html
2|KECo1q|https://stackoverflow.com/questions/61378005/decrypting-aes-256-cbc-cipher-with-a-passcode-built-using-pbkdf2-in-python
sqlite> 
```
Enjoy!