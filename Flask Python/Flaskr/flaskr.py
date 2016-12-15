
""" LINK FOR THE TUTORIAL FOLLOWED : http://flask.pocoo.org/docs/0.11/tutorial/ """

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#create the application
app = Flask(__name__)
app.config.from_object(__name__)

#overload default config and update config from an environment variable
app.config.update( dict(
     DATABASE = os.path.join(app.root_path, 'flaskr.db')
     SECRET_KEY = 'development key'
     USER_NAME = 'admin'
     password = 'default'
	))

app.config.from_envvar('FLASKR SETTINGS', silent= True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

