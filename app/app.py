from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app  = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# 'sqlite:///data.db'

db = SQLAlchemy(app)

from app.routes import *

# if __name__ == "__main__":
    # app.run(debug=True)