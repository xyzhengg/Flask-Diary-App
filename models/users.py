import db

def add_user(firstname, lastname, email, password_hash, diarycode):
    db.sql_write(
        'INSERT INTO users (first_name, last_name, email, password_hash, diary_code) VALUES (%s, %s, %s, %s, %s)',
        [firstname, lastname, email, password_hash, diarycode]
    )

def get_user_by_email(email):
    user = db.sql_select_one('SELECT * FROM users WHERE email=%s', [email])
    return user

def check_user_exists(email):
    result = db.sql_select_one('SELECT * FROM users WHERE email=%s', [email])
    return bool(result)

def get_username_join_diary_users(user_id):
    user = db.sql_select_one('SELECT first_name FROM users INNER JOIN entries ON users.id = entries.user_id WHERE entries.user_id = %s', [user_id])
    return user
