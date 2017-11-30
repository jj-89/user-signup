from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate-info")
def index():
    return render_template('signup-form.html', title="User Signup",username = '', username_error = '',
password = '', pw1_error = '', verify = '', pw2_error = '', email = '', email_error = '')

@app.route("/validate-info", methods=['POST'])
def validate_info():
    username = request.form['username']
    password1 = request.form['password']
    password2 = request.form['verify']
    email = request.form['email']

    username_error = ''
    pw1_error = ''
    pw2_error = ''
    email_error = ''


    # Validate username

    # test lengh of username
    if len(username) == 0:
        username_error = "Please choose a user name"
        username = ''
    elif len(username) < 3 and len(username) > 0:
        username_error = "Username must be at least three characters"
        username = ''
    elif len(username) > 20:
        username_error = "Username must be less than twenty characters"
        username = ''

        
    
    # check username for spaces
    for char in username:
        if char == " ":
            username_error = "Username can not contain spaces"
            username = ''

    # Validate Password
    # test length of password
    if len(password1) == 0:
        pw1_error = "Please enter a password"
        password1 = ''
    elif len(password1) < 3 and len(password1) > 0:
        pw1_error = "Password must be at least three characters"
        password1 = ''
    elif len(password1) > 20:
        pw1_error = "Password must be less than twenty characters"
        password1 = ''
    # check password for spaces
    for char in password1:
        if char == " ":
            pw1_error = "Password can not contain spaces"
            password1 = ''
    # verify password is correct
    if password1 != password2:
        pw2_error = "Your password was not typed correctly"
        password1 = ''
        password2 = ''


    # validate email
    #check format
    required_characters = ['@','.']
    if '@' not in email or '.' not in email:
        email_error = "Please input a valid email."
    # tests lengh of email
    if len(email) < 3 and len(email) > 0:
        email_error = "Your email must be at least three characters"
        email = ''
    elif len(password1) > 20:
        email_error = "Your email must be less than twenty characters"
        email = ''
    # check password for spaces
    for char in email:
        if char == " ":
            email_error = "Password can not contain spaces"
            email = ''


    if not username_error and not pw1_error and not pw2_error and not email_error:
        username = request.form['username']
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup-form.html',username=username, username_error=username_error,pw1_error=pw1_error,
    pw2_error=pw2_error,email_error=email_error)

@app.route('/welcome')
def welcome():
    username= request.form.get('username')
    return render_template('welcome.html',username=username)



app.run()