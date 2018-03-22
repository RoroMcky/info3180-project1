"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import ProfileForm
from models import UserProfile
from werkzeug.utils import secure_filename
from models import UserProfile
import os
import datetime

###
# Routing for your application.
###
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile',methods=["POST", "GET"])
def profile():
    import datetime
    form = ProfileForm()
    uFolder = app.config['UPLOAD_FOLDER']
    
    if request.method == "POST" and form.validate_on_submit():
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Gender = request.form['Gender']
        Email = request.form['Email']
        Location = request.form['Location']
        Biography = request.form['Biography']
        created_on = str(datetime.datetime.now()).split()[0]
        
        image_file = request.files['photo']
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(uFolder, filename))
        user = UserProfile(FirstName, LastName, Gender, Email, Location, Biography, filename, created_on)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Profile was sucessfully added!', 'sucess')
        return redirect('/profiles')
    return render_template('profile.html', form=form) 
    
@app.route('/profiles')
def profiles():
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html', users=users)
    
@app.route('/profile/<userid>')
def individual(userid):
    users = UserProfile.query.filter_by(id=userid).first()
    return render_template('profiles.html', users=users)
    

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")