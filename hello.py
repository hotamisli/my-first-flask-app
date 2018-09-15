from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "index page"

@app.route('/hello')
def hello():
    return "hello"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/user/<int:id>')
def show_user_id(id):
    return 'User %s' % id

@app.route('/projects/')
def projects():
    return ' The Projects page'
