#!/bin/env python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database instance
db = SQLAlchemy(app)

# Define database models
class Message(db.Model): # Guestbook messages ^-^ rn they js have a message n an author
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(100), unique=False, nullable=False)
	author = db.Column(db.String(100), unique=False, nullable=False)

	def __repr__(self):
		return f"Message: {self.message} Author: {self.author}"

@app.route('/')
def index():
	messages = Message.query.all()
	return render_template('index.html', messages=messages)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blog')
def get_post():
	post_id = request.args.get("post")
	return render_template(f'/blog/{post_id}.html')

@app.route('/add_data')
def add_data():
	return render_template('add_profile.html')

@app.route('/message', methods=["POST"])
def message():
        message = request.form.get("note")
        author = request.form.get("author")
        if message != '' and author != '':
                m = Message(message=message, author=author)
                db.session.add(m)
                db.session.commit()
                return redirect('/')
        else:
                return redirect('/')

@app.route('/erase/<int:id>')
def erase_message(id):
        data = db.session.get(Message, id)
        db.session.delete(data)
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(host="0.0.0.0", port=5000)
