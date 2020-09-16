from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

""" App route indicates string to access a certain page
    to indicate a variable surround the variable in <>
    ex. <username> to get an arbitrary username
    to specify the variable's type: <varType:name> where the type is something like a string or int """

@app.route('/')
def hello_world():
    return 'Main page'

@app.route('/hello')
def hello():
    # render a created html file from "templates" folder
    return render_template('hello.html')

@app.route('/hello/<user>')
def hello_user(user):
    # render template with additional parameters
    return render_template('hello.html', name=escape(user))

@app.route('/user/<username>')
def show_user_profile(username):
    # Return specified user page
    return 'User %s' % escape(username)

def valid_login():
    #riveting functionality here I know
    return True

# adding additional parameter to route indicating supported HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login():
            return 'You logged in'

        return 'Invalid login information'

    return 'Nothing here'


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # Show post with specified id
    return 'Post %d' % post_id

@app.route('/user/<path:subpath>')
def show_subpath(subpath):
    # Show the subpath after /hello/
    return 'Subpath %s' % escape(subpath)

# Printing tests for different paths
# simulating webapp handling requests
with app.test_request_context():
    print(url_for('show_user_profile', username='Jaeg6'))
    print(url_for('show_post', post_id=123))
    print(url_for('show_subpath', subpath='path/next'))

# Testing context locals and sending requests with POST method
with app.test_request_context('/login', method='POST'):
    assert request.path == '/login'
    assert request.method == 'POST'

# more request functionality found in login() function

if __name__ == '__main__':
    app.run()
