from flask import render_template
# terminal - pip3 install flask
from application import app


@app.route('/')
def index():
    return "Hello from Flask"


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group="The Group")


@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title="Favourites", favourite_things=["Food", "Dogs", "Sleeping", "Snacks"])


@app.route('/about')
def about():
    return render_template('about.html')

