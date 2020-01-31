from flask import request, redirect, render_template, url_for, flash
from flaskapp import db, app
from flaskapp.forms import RegistrationForm
from flaskapp.models import Message

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.first_name.data + form.last_name.data
        email = form.email.data
        message = form.message.data

        new_commit = Message(name=name, email=email, message=message)
        db.session.add(new_commit)
        db.session.commit()

        flash("mesage delivered", 'success')

    return render_template("home.html", form=form)

@app.route("/highlights")
def highlights():
    return render_template("highlights.html")
    