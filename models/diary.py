import db

def check_diary_code_exist(diarycode):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE diary_code =%s',
        [diarycode]
    )
    return bool(result)

def check_new_diary_code_exist(new_diary_code):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE diary_code =%s',
        [new_diary_code]
    )
    return bool(result)

def check_email_2_exists(email):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE email_2 =%s',
        [email]
    )
    return bool(result)

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