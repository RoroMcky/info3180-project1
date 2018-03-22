from . import db


class UserProfile(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,unique=True)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    Gender = db.Column(db.String(80))
    Email= db.Column(db.String(255))
    Location=db.Column(db.String(80))
    Biography=db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    picture= db.Column(db.String(80))
    
    
def __init__(self, FirstName, LastName, Gender, Email, Location, Biography, created_on, picture):
    self.FirstName= FirstName
    self.LastName = LastName
    self.Gender = Gender
    self.Email = Email
    self.Location = Location
    self.Biography = Biography
    self.created_on = created_on
    self.picture = picture
    

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

def __repr__(self):
        return '<User %r>' % (self.username)
