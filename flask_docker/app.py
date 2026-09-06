#!/bin/env python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bunny:H0lyFw1ck!@db:5432/sitedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define Database Models
class Message(db.Model): # Guestbook messages ^-^ rn they js have a message n an author
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(100), unique=False, nullable=False)
	author = db.Column(db.String(100), unique=False, nullable=True)
	date_posted = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, message, author, date_posted):
		self.message = message
		self.author = author
		self.date_posted = date_posted

	def __repr__(self):
		return f"Message: {self.message} Author: {self.author}"

class BlogPost(db.Model): # Blog Posts should take an id (obvs), a title 4 sidebar display, n a date
	__tablename__ = 'blog-posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, unique=True, nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, title, date_posted):
		self.title = title
		self.date_posted = date_posted

	def __repr__(self):
		return f"Title: {self.title}"

# Define App Routes

@app.route('/')
def index():
	messages = Message.query.all()
	posts = BlogPost.query.all()
	return render_template('index.html', messages=messages, posts=posts)

@app.route('/about')
def about():
	posts = BlogPost.query.all()
	return render_template('about.html', posts=posts)

@app.route('/blog/<title>')
def get_post(title):
	post = db.one_or_404(db.select(BlogPost).filter_by(title=title))
	posts = BlogPost.query.all()
	return render_template(f'/blog/{post.id}.html', posts=posts, current=title)

@app.route('/add_data')
def add_data():
	return render_template('add_profile.html')

@app.route('/message', methods=["POST"])
def message():
	message = request.form.get("note")
	author = request.form.get("author")
	date_posted = datetime.now()
	if message != '' and author != '':
		m = Message(message=message, author=author, date_posted=date_posted)
		db.session.add(m)
		db.session.commit()
		return redirect('/')
	elif message != '' and author == '':
		am = Message(message=message, author="Anonymous", date_posted=date_posted)
		db.session.add(am)
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
