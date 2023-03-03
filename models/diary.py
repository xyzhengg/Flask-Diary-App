import db

def check_diary_code_exist(diary_code):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE diary_code =%s',
        [diary_code]
    )
    return bool(result)

def check_new_diary_code_exist(new_diary_code):
    result = db.sql_select_one(
        'SELECT * FROM diary WHERE diary_code =%s',
        [new_diary_code]
    )
    return bool(result)

def add_email_2_to_diary(email, diarycode):
    db.sql_write(
        'UPDATE diary SET email_2 = %s WHERE diarycode = %s',
        [email, diarycode]
    )


