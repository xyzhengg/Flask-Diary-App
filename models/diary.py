import db

def check_diary_code_exist(diarycode):
    result = db.sql_select_one(
        'SELECT diary_code FROM diary WHERE diary_code =%s',
        [diarycode]
    )
    return result['diary_code']

def check_new_diary_code_exist(new_diary_code):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE diary_code =%s',
        [new_diary_code]
    )
    return result

def check_email_2_exists(diarycode):
    result = db.sql_select_one(
        'SELECT email_2 FROM diary WHERE diary_code = %s',
        [diarycode]
    )
    return result['email_2']

def add_email_2_to_diary(email, diarycode):
    db.sql_write(
        'UPDATE diary SET email_2 = %s WHERE diary_code = %s',
        [email, diarycode]
    )

def add_email_1_to_diary(diarycode, email):
    db.sql_write(
        'INSERT INTO diary (diary_code, email_1) VALUES (%s, %s)',
        [diarycode, email]
    )