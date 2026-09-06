#!/bin/env python3

# Imports
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from pathlib import Path

# App !
app = Flask(__name__)

# Read config file in home directory (upload 2 NAS !)
config_path = Path(__file__).parent / "app_config.txt"
config_file = open(config_path, "r", encoding="utf-8")
config_lines = config_file.readlines()

# Set config variables
key = config_lines[1].rstrip()
db_user = config_lines[3].rstrip()
db_pass = config_lines[5].rstrip()

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@db:5432/sitedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = f'{key}'


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

@app.route('/') # Serve the home page and take in all database models
def index():
	messages = Message.query.all() # Allow serving of guestbook messages
	posts = BlogPost.query.all() # Enable automatic updating of blog sidebar when posts are added
	return render_template('index.html', messages=messages, posts=posts)

@app.route('/about') # Serve the about me page ! (might put this in blog eventually, idk)
def about():
	posts = BlogPost.query.all() # Enable blog
	return render_template('about.html', posts=posts)

@app.route('/blog/<title>') # Serve specific blog post based on the title of the post
def get_post(title):
	post = db.one_or_404(db.select(BlogPost).filter_by(title=title)) # Get the post by its title
	posts = BlogPost.query.all() # Allow serving of blog posts
	return render_template(f'/blog/{post.id}.html', posts=posts, current=title) # takes in post object and
										# currently displayed posts title

@app.route('/add_data') # Serve guestbook form
def add_data():
	return render_template('add_profile.html')

@app.route('/message', methods=["POST"]) # Add message provided from form
def message():
	message = request.form.get("note") # Retrieves the message content from the sent form
	author = request.form.get("author") # Retrieves the author from the sent form
	date_posted = datetime.now() # Sets the date of the message
	if message != '' and author != '': # If author is provided, display it
		m = Message(message=message, author=author, date_posted=date_posted)
		db.session.add(m)
		db.session.commit()
		return redirect('/')
	elif message != '' and author == '': # If author is not provided, set the author as Anonymous
		am = Message(message=message, author="Anonymous", date_posted=date_posted)
		db.session.add(am)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')


# Initialize The Database & The App

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(host="0.0.0.0", port=5000)
