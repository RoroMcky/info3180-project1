from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:chuchi1996@localhost/profile"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = '.app/static/uploads'

db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

app.config.from_object(__name__)
from app import views
