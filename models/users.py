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

def get_all_username(diary_id):
    users = db.sql_select('SELECT first_name, id FROM users WHERE diary_code=%s', [diary_id])
    return users

def isValidEmail(email):
    atindex = email.find("@")
    postatlen = len(email[atindex:])
    dotindex = email[atindex:].find(".")
    seconddotindex = email[atindex:].rfind(".")
    if email.count('@') == 1 and atindex >=1 and "." in email[atindex:] and dotindex > 1 and postatlen - seconddotindex > 1:
        return True
    return False