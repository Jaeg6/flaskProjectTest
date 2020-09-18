from flask import Flask, url_for, request, render_template, redirect, session
from markupsafe import escape
from admin.bluprnt import bluprnt

app = Flask(__name__)

""" App route indicates string to access a certain page
    to indicate a variable surround the variable in <>
    ex. <username> to get an arbitrary username
    to specify the variable's type: <varType:name> where the type is something like a string or int """

# registering the blueprint found in the bluprnt.py file (see admin package)
# the url_prefix indicates the route prefix before being able to access the routes within the blueprint
# ex ~/blu won't work, you need to put ~/bp/blu instead
app.register_blueprint(bluprnt, url_prefix="/bp")

# Secret key for session
app.secret_key = "1234"

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

@app.route('/user')
def show_user_profile():
    # Return specified user page
    if "user" in session:
        user = session["user"]
        return 'User: %s' % user
    else:
        return redirect(url_for("login"))

# adding additional parameter to route indicating supported HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # user entered information to text box on the page, get this info
        # request.form will be items found within the form of the html file from the POST request
        user = request.form["nm"]

        if user == "":
            return render_template("login.html")

        # storing username to this session
        session["user"] = user
        return redirect(url_for("show_user_profile"))
    else:
        # GET request, bring user to login page
        return render_template("login.html")


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
