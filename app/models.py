from . import db


class UserProfile(db.Model):
    
    id = db.Column(db.Integer, primary_key=True,unique=True)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    Gender = db.Column(db.String(80))
    Email= db.Column(db.String(255))
    Location=db.Column(db.String(80))
    Biography=db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    picture= db.Column(db.String(80))
    
    __tablename__ = 'user'
    
    def __init__(self,f_name, l_name, gender, email, location, bio, joined, img_name):
        self.FirstName= f_name
        self.LastName = l_name
        self.Gender = gender
        self.Email = email
        self.Location = location
        self.Biography = bio
        self.created_on = joined
        self.picture = img_name
    

    
