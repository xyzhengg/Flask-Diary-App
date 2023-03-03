from flask import Flask, render_template, request, redirect, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash 

from models.users import add_user, get_user_by_email


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug = True)
app.config['SECRET_KEY'] = 'ultra mega secret key for diary'

#Don't allow 
# @app.before_request
# def is_user_logged_in():
#     path = request.path
#     if path != '/login' and path != '/static/style.css' and session.get('user_id') is None:
#         return redirect ('/login')


## Main diary page
@app.route('/')
def index():
    if session.get('user_id') is None:
        return redirect ('/landing') 
    return render_template('landing.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.post('/logout')
def logout():
    session.pop('user_id')
    session.pop('user_name')
    session.pop('user_email')
    print(session)
    return redirect('/login')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        user = get_user_by_email(email)
        password_matches = check_password_hash(user['password_hash'], password)

        if password_matches:
            session['user_id'] = user['id']
            session['user_name'] = user['firstname']
            session['user_email'] = user['email']
            print(session)
            return redirect('/')
        else:
            login_error = "Your email or password is incorrect. Please try again"
            return login_error
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        password = request.form.get('password')
        passwordcheck = request.form.get('passwordcheck')
        password_hash = generate_password_hash(password)
        if password != passwordcheck:
            error = "Passwords do not match. Please try again."
            return error
        firstname = request.form.get('firstname').lower()
        lastname = request.form.get('lastname').lower()
        email = request.form.get('email').lower()
        diarycode = request.form.get('diarycode')

        add_user(firstname, lastname, email, password_hash, diarycode)
        return redirect('/login')
    return render_template('signup.html')