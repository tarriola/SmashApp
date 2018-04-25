from flask import Flask, render_template

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

app.config.from_object('config')

# Define the database object
db = SQLAlchemy(app)

from app.site.views import mod

app.register_blueprint(mod)

# Build the data database
# This will create the database file using SQLAlchemy
db.create_all()
