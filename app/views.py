"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import ProfileForm
from models import UserProfile
from werkzeug.utils import secure_filename
from models import UserProfile
import os
import datetime


###
# Routing for your application.
###

@app.route('/profile/', methods=["POST", "GET"])
def profile():
        form = ProfileForm()
        uFolder = app.config['UPLOAD_FOLDER']
        if request.method == "POST":
            if form.validate_on_submit():
                f_name = request.form['FirstName']
                l_name = request.form['LastName']
                gender = request.form['Gender']
                email = request.form['Email']
                location = request.form['Location']
                bio = request.form['Biography']
                now = datetime.datetime.now()
                joined = "" + format_date_joined(now.year, now.month, now.day)
                img=request.files['picture']
                img_name= secure_filename(img.filename)
                img.save(os.path.join(uFolder,img_name))
                user = UserProfile(f_name, l_name, gender, email, location, bio, joined, img_name)
                
                db.session.add(user)
                db.session.commit()
                flash('Profile was sucessfully added.', 'success')
                return redirect(url_for('profiles'))
            
            flash(form.errors.items(), 'danger')
            return render_template('profile.html', form=form)
            
        return render_template('profile.html', form=form) 
        
@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    users=db.session.query(UserProfile).all()
    return render_template('profiles.html', users=users)
    
@app.route('/profiles/<userid>', methods=["GET", "POST"])
def individual(userid):
    userid = str(userid)
    user = UserProfile.query.filter_by(id=userid).first()
    return render_template('individual.html', user=user)
    
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))
    
def format_date_joined(year, month, day):
    date_joined = datetime.date(year, month, day)
    return date_joined.strftime("%B %d, %Y")   

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
