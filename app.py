from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime
import calendar
from cloudinary import CloudinaryImage
import cloudinary.uploader
import mistletoe

# with open('foo.md', 'r') as fin:
#     rendered = mistletoe.markdown(fin)

from models.users import add_user, get_user_by_email, check_user_exists, get_username_join_diary_users, get_all_username
from models.diary import check_diary_code_exist, add_email_2_to_diary, check_new_diary_code_exist, check_email_2_exists, add_email_1_to_diary
from models.posts import add_entry, get_all_posts, get_single_post, edit_entry, delete_entry
from models.images import insert_many_images, get_all_images, delete_all_images, get_one_image

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug = True)
app.config['SECRET_KEY'] = 'ultra mega secret key for diary'


def generate_diary_code():
    new_diary_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return new_diary_code

#Don't allow 
# @app.before_request
# def is_user_logged_in():
#     path = request.path
#     if path != '/login' and path != '/static/style.css' and session.get('user_id') is None:
#         return redirect ('/login')

@app.post('/delete-images')
def delete_images():
    if session.get('user_id') is None:
        return redirect ('/landing')
    post_id = int(request.form.get('post_id'))
    delete_all_images(post_id)
    return redirect(f'/view/{post_id}')

@app.post('/delete')
def delete():
    if session.get('user_id') is None:
        return redirect ('/landing')
    post_id = int(request.form.get('post_id'))
    delete_all_images(post_id)
    delete_entry(post_id)
    return redirect ('/')

@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if session.get('user_id') is None:
        return redirect ('/landing')
    post = get_single_post(post_id)
    print(post)
    poster_id = post['user_id']
    fav = post['fav']
    if session.get('user_id') != poster_id:
        return redirect ('/')
    
    entry_id = post['id']
    image_list = get_all_images(entry_id)

    diary_heading = post['diary_heading']
    diary_text = post['diary_text']

    if request.method == 'GET':
    # Image placeholder
        post_date = str(post['post_time'])[:10]
        post_time = str(post['post_time'])[11:16]
        date = int(post_date[-2:])
        month = int(post_date[5:7])
        year = int(post_date[:4])

        day = calendar.weekday(year, month, date)
        day_name = calendar.day_name[day]

        return render_template('edit.html',
            poster_id = poster_id,
            diary_heading = diary_heading,
            diary_text = diary_text,
            post_time = post_time,
            post_id = post_id,
            post_date = post_date,
            day_name = day_name,
            image_list = image_list)


    if request.method == 'POST':
    # Displaying the month name in html dropdown
        new_date = request.form.get('date')
        new_time = request.form.get('time')
        new_timedate_str = f"{new_date} {new_time}"
        print(new_timedate_str)
        new_timedate = datetime.strptime(new_timedate_str, '%Y-%m-%d %H:%M')

        images = request.files.getlist('images')
        new_heading = request.form.get('heading')
        new_text = request.form.get('entry')

        post_id = edit_entry(new_heading, new_text, fav, new_timedate, post_id)
        # delete_all_images(post_id)
        
        image_rows = []
        for image in images: 
            uploaded_image = cloudinary.uploader.upload(image)
            image_rows.append([uploaded_image['public_id'], uploaded_image['url'], post_id])
        insert_many_images(image_rows)


        return redirect(f'/view/{post_id}')
                           
@app.route('/view/<post_id>')
def view_post(post_id):
    user_id = session.get('user_id')
    user_name = session.get('user_name').capitalize()
    if session.get('user_id') is None:
        return redirect ('/landing')
    
    post = get_single_post(post_id)
    poster_id = post['user_id']
    diary_heading = post['diary_heading'].capitalize()
    diary_text = post['diary_text']

    entry_id = post['id']
    image_list = get_all_images(entry_id)

    post_date = str(post['post_time'])[:10]
    reversed_date = post_date[-2:] + '-' + post_date[5:7] + '-' + post_date[:4]
    post_time = str(post['post_time'])[11:16]
    first_name = str(get_username_join_diary_users(poster_id)['first_name']).capitalize()
    date = int(post_date[-2:])
    month = int(post_date[5:7])
    year = int(post_date[:4])
    day = calendar.weekday(year, month, date)
    day_name = calendar.day_name[day]

    return render_template('view.html',
                    user_id = user_id,
                    user_name = user_name,
                    poster_id = poster_id,
                    diary_heading = diary_heading,
                    diary_text = diary_text,
                    post_time = post_time,
                    reversed_date = reversed_date,
                    first_name = first_name,
                    post_id = post_id,
                    day_name = day_name,
                    image_list=image_list
                    )

@app.route('/')
def redirecttomain():
    diary_id = session.get('diary_id')
    if session.get('user_id') is None:
        return redirect ('/landing')
    return redirect(f'/diary/{diary_id}')

## Main diary page
@app.route('/diary/<diary_id>')
def index(diary_id):
    if session.get('user_id') is None:
        return redirect ('/landing')
    diary_id = session.get('diary_id')
    users = get_all_username(diary_id)
    user_one = users[0]['first_name'].capitalize()
    user_two = users[1]['first_name'].capitalize()

    data = get_all_posts(diary_id)
    if len(data) < 4:
        random_posts = data
    else:
        random_posts = random.sample(data, 4)
        for random_post in random_posts:
            random_id = random_post['id']
            random_photo = get_one_image(random_id)
            if random_photo is not None:
                random_url = random_photo['img_url']
            else: 
                random_photo = {'img_url': 'https://res.cloudinary.com/ddg0iss6e/image/upload/v1678273766/Screen_Shot_2023-03-08_at_10.08.54_pm_yz0hez.png'}
                random_url = random_photo['img_url']            
            random_post['image_data'] = {'img_url': random_url}


    if len(data) > 0:
        sorted_posts = {}
        for post_list in data:
            post_date = str(post_list['post_time'])[:10]
            date = int(post_date[-2:])
            month_num = int(post_date[5:7])
            year = int(post_date[:4])
            day = calendar.weekday(year, month_num, date)
            day_name = calendar.day_name[day]
            month_name = calendar.month_name[month_num]
            full_date = str(date) + ' ' + month_name + ' ' + str(year) +  ', ' + day_name 
            if full_date in sorted_posts:
                sorted_posts[full_date].append(post_list)
            else:
                sorted_posts[full_date] = [post_list]

        for date in sorted_posts:
            for post in sorted_posts[date]:
                post_id=post['id']
                user_id = post['user_id']
                time = str(post['post_time'])[11:16]
                first_name = str(get_username_join_diary_users(user_id)['first_name']).capitalize()
                image_list = get_all_images(post_id)

                post['metadata'] = {'first_name': first_name, 'time': time, 'images': image_list}


        return render_template('main.html', 
                           diary_id = diary_id,
                           user_one = user_one,
                           user_two = user_two,
                           sorted_posts = sorted_posts,
                           random_posts=random_posts,
                           post_date=post_date,)
    no_post_error = "You have no posts! Get started by creating an entry"
    return render_template('main.html', 
                           diary_id = diary_id,
                           no_post_error = no_post_error)

@app.route('/addentry', methods=['GET', 'POST'])
def addentry():
    if session.get('user_id') is None:
        return redirect ('/login')
    if request.method == 'GET':
        return render_template('new_entry.html')
    if request.method == 'POST':
        diary_code = session.get('diary_id')
        user_id = session.get('user_id')
        diary_heading = request.form.get('heading')
        diary_text = request.form.get('entry')

        entry_id = add_entry(diary_code, user_id, diary_heading, diary_text) 

        images = request.files.getlist('images')
        if len(images) > 0:
            image_rows = []
            for image in images:
                if image.filename != '': 
                    uploaded_image = cloudinary.uploader.upload(image)
                    image_rows.append([uploaded_image['public_id'], uploaded_image['url'], entry_id['id']])
                insert_many_images(image_rows)

        return redirect(f'/diary/{diary_code}')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.post('/logout')
def logout():
    session.pop('user_id')
    session.pop('user_name')
    session.pop('user_email')
    session.pop('diary_id')
    return redirect('/login')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    password = 'heyhey'
    password_hash = generate_password_hash(password)
    print(password_hash)
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        check_exists = check_user_exists(email)
        user = get_user_by_email(email)

        if user is not None:
            password_matches = check_password_hash(user['password_hash'], password)
        if not check_exists or not password_matches:
            login_error = "Your email or password is incorrect. Please try again"
            return render_template('login.html', login_error = login_error)
        if check_exists and password_matches:
            session['user_id'] = user['id']
            session['user_name'] = user['first_name']
            session['user_email'] = user['email']
            session['diary_id'] = user['diary_code']
            diary_id = session.get('diary_id')
            print(session)
            return redirect(f'/diary/{diary_id}')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if session.get('user_email'):
        return redirect('/')
    if request.method == 'POST':
        firstname = request.form.get('firstname').lower()
        lastname = request.form.get('lastname').lower()
        email = request.form.get('email').lower()
        password = request.form.get('password')
        passwordcheck = request.form.get('passwordcheck')
        password_hash = generate_password_hash(password)
        diarycode = ''.join(request.form.get('diarycode')).upper()

        if check_user_exists(email):
            account_exists_error = "You already have an account. Please sign in"
            return render_template('signup.html', account_exists_error = account_exists_error)
        
        else: 
            if password != passwordcheck:
                error = "Passwords do not match. Please try again."
                return render_template('signup.html', error = error)
            
            if len(diarycode) == 0:
                new_diary_code = generate_diary_code()
                while check_new_diary_code_exist(new_diary_code):
                    new_diary_code = generate_diary_code()
                diarycode = new_diary_code
                add_user(firstname, lastname, email, password_hash, diarycode)
                add_email_1_to_diary(diarycode, email)

                return render_template('signupsuccess.html', 
                                    firstname = firstname,
                                    diarycode = diarycode)

            if len(diarycode) == 8:
                if check_diary_code_exist(diarycode) and check_email_2_exists(email) == False:
                    add_user(firstname, lastname, email, password_hash, diarycode)
                    add_email_2_to_diary(email, diarycode)
                    return render_template('signupsuccess.html', 
                                    firstname = firstname,
                                    diarycode = diarycode)
                else:
                    email_2_error = "Cannot add you to the diary. Please contact owner"
                    return render_template('signup.html', email_2_error = email_2_error)
                
            elif len(diarycode) != 8 and len(diarycode) != 0:
                diarycode_error = "Your diary code does not exist. Please try again"
                return render_template('signup.html', diarycode_error = diarycode_error)

    return render_template('signup.html')
