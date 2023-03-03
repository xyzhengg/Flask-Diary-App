import db

def add_user(firstname, lastname, email, password_hash, diarycode):
    db.sql_write(
        'INSERT INTO users (firstname, lastname, email, password_hash, diarycode) VALUES (%s, %s, %s, %s, %s)',
        [firstname, lastname, email, password_hash, diarycode]
    )

def get_user_by_email(email):
    user = db.sql_select_one('SELECT * FROM users WHERE email=%s', [email])
    return user