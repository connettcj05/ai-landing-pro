import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    from models import Newsletter
    email = request.form.get('email')
    if email:
        subscriber = Newsletter(email=email)
        try:
            db.session.add(subscriber)
            db.session.commit()
            flash('Thanks for subscribing!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error subscribing. Please try again.', 'error')
            logging.error(f"Subscribe error: {str(e)}")
    return redirect(url_for('index'))

@app.route('/contact', methods=['POST'])
def contact():
    from models import Contact
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if name and email and message:
        contact = Contact(name=name, email=email, message=message)
        try:
            db.session.add(contact)
            db.session.commit()
            flash('Message sent successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error sending message. Please try again.', 'error')
            logging.error(f"Contact error: {str(e)}")
    return redirect(url_for('index'))

with app.app_context():
    import models
    db.create_all()
