#!/usr/bin/env python3

# Imports
from datetime import datetime, timedelta, timezone
from pathlib import Path

from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# App !
app = Flask(__name__)

# Read config file in home directory (upload 2 NAS !)
config_path = Path(__file__).parent / "app_config.txt"
#config_file = open(config_path, "r", encoding="utf-8")
#config_lines = config_file.readlines()
with open(config_path, "r", encoding="utf-8") as config_file:
	config_lines = config_file.readlines()
# Set config variables
key = config_lines[1].rstrip()
db_user = config_lines[3].rstrip()
db_pass = config_lines[5].rstrip()
admin_user = config_lines[7].rstrip()
admin_pword = config_lines[9].rstrip()

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@db:5432/sitedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = f'{key}'


# Database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db) # I dont think this is necessary the way things r set up rn, but who knows

# Music Player Playlist
playlist = {
	1: ("LosT.mp3", "LosT - Bring Me The Horizon"),
	2: ("No Love In LA.mp3", "No Love In LA - Palaye Royale"),
	3: ("Detroit.mp3", "Detroit - Badflower"),
	4: ("Modern Life Is Lonely.mp3", "Modern Life Is Lonely - Holding Absence")
}

# Global variables
login_fail = ""
admin_logged_in = False

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

class WebButton(db.Model): # Idk how 2 store images so itll just take in the name of the file as well as an id
	__tablename__ = 'web_buttons'			# (Might b temporary if i ever figure out a better way)

	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(100), unique=True, nullable=False)

	def __init__(self, filename):
		self.filename = filename

	def __repr__(self):
		return f"File: {self.filename}"

# Define App Routes
@app.route('/') # Serve the home page and take in all database models
def index():
	messages = Message.query.all() # Allow serving of guestbook messages
	posts = BlogPost.query.all() # Enable automatic updating of blog sidebar when posts are added
	web_buttons = WebButton.query.all() # Grab filenames 2 avoid endless copy-pasting
	song = playlist
	return render_template('index.html', messages=messages, posts=posts, web_buttons=web_buttons, song=song)

@app.route('/about') # Serve the about me page ! (might put this in blog eventually, idk)
def about():
	posts = BlogPost.query.all()
	web_buttons = WebButton.query.all()
	return render_template('about.html', posts=posts, web_buttons=web_buttons)

@app.route('/blog/<title>') # Serve specific blog post based on the title of the post
def get_post(title):
	post = db.one_or_404(db.select(BlogPost).filter_by(title=title)) # Get the post by its title
	posts = BlogPost.query.all()
	web_buttons = WebButton.query.all()
	return render_template(f'/blog/{post.id}.html', posts=posts, current=title, web_buttons=web_buttons)
								# takes in post object and
								# currently displayed posts title

@app.route('/admin')
def admin():
	web_buttons = WebButton.query.all()
	login_fail = ""
	return render_template('admin_login.html', web_buttons=web_buttons, login_fail=login_fail)

@app.route('/admin_login', methods=["POST"])
def admin_login():
	global admin_logged_in
	web_buttons = WebButton.query.all()
	username = request.form.get('admin-user')
	password = request.form.get('admin-pword')
	if username == f'{admin_user}' and password == f'{admin_pword}':
		admin_logged_in = True
		return redirect('/moderation-panel')
	else:
		login_fail = "Login Failed (stop pls ^~^;)"
		return render_template('admin_login.html', web_buttons=web_buttons, login_fail=login_fail)

# SECTION FOR MOD PANEL ACTIONS
@app.route('/moderation-panel')
def blog_manager():
	global admin_logged_in
	posts = BlogPost.query.all()
	web_buttons = WebButton.query.all()
	messages = Message.query.all()
	if admin_logged_in:
		admin_logged_in = False
		return render_template('moderation_panel.html', posts=posts, web_buttons=web_buttons, messages=messages)
	else:
		return redirect('/admin')

@app.route('/create-blog-post', methods=["POST"])
def add_post():
	title = request.form.get("title")
	time_offset = -4.0
	tzinfo = timezone(timedelta(hours=time_offset))
	date_posted = datetime.now(tzinfo)
	if title != '':
		p = BlogPost(title=title, date_posted=date_posted)
		db.session.add(p)
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/edit-blog-title/<int:id>', methods=["POST"])
def new_title(id):
	new_title = request.form.get("new-title")
	time_offset = -4.0
	tzinfo = timezone(timedelta(hours=time_offset))
	new_date_posted = datetime.now(tzinfo)
	if new_title != '':
		p = db.session.get(BlogPost, id)
		p.title = new_title
		p.date_posted = new_date_posted
		db.session.commit()
		return redirect('/')
	else:
		return redirect('/')


@app.route('/erase-blog-id/<int:id>')
def erase_post(id):
	data = db.session.get(BlogPost, id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')

@app.route('/erase-message/<int:id>')
def erase_message(id):
	data = db.session.get(Message, id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')

@app.route('/add_data') # Serve guestbook form
def add_data():
	return render_template('add_profile.html')

@app.route('/message', methods=["POST"]) # Add message provided from form
def message():
	message = request.form.get("note") # Retrieves the message content from the sent form
	author = request.form.get("author") # Retrieves the author from the sent form
	time_offset = -4.0
	tzinfo = timezone(timedelta(hours=time_offset))
	date_posted = datetime.now(tzinfo) # Sets the date of the message
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
