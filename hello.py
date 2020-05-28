from flask import Flask, url_for, request, render_template
from markupsafe import Markup, escape

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    
    return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context('/hello', method='POST'):
    # Now you can do something with the request until the
    # Enf of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

with app.request_context(environ):
    assert request.method == 'POST'