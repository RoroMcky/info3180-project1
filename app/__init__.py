from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qvsalsodhvwsdk:64fab8d09bf9880dc4bd4f9843037aa9ad55aa1f1714a004a8a0542bfdc970b7@ec2-54-243-130-33.compute-1.amazonaws.com:5432/d4406j2g57hgc3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views