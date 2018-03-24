from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kqofejodmtaycl:c1ef6e35fd481fc4d749011a6d3c5a6d954c01941b4abd162f857dd48a6f918f@ec2-54-243-130-33.compute-1.amazonaws.com:5432/dbiqtmvh58rhqr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views