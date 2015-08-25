# flask-login-try
Try logins on a Flask app, similar to http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

Requires: 
* pip install --user Flask-WTF
* pip install --user Flask-SQLAlchemy
* pip install --user migrate
* pip install --user sqlalchemy-migrate



* Add config.py to your .gitignore
* Copy config.py.EXAMPLE to config.py

config.py.EXAMPLE contains the following
```
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
```

Edit your config.py so that the SECRET_KEY is some random string of letters and numbers such as '89fwwce48LSI2h8'

Leave the other line alone.
