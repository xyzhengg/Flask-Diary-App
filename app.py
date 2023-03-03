from flask import Flask, render_template, request, redirect, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ultra mega secret key for diary'

#Don't allow 
# @app.before_request
# def is_user_logged_in():
#     path = request.path
#     if path != '/login' and path != '/static/style.css' and session.get('user_id') is None:
#         return redirect ('/login')


##Landing page
@app.route('/')
def index():
    return "Hello world!"

@app.route('/login')


@app.route('/signup')


@app.route('/')

if __name__ == "__main__"
    app.run(debug = True)

