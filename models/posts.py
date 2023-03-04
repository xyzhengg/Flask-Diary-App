import db

def add_entry(diary_code, user_id, diary_heading, diary_text, image_url, post_time):
    db.sql_write(
        'INSERT INTO posts (diary_code, user_id, diary_heading, diary_text, image_url, post_time) VALUES (%s, %s, %s, %s, %s, %s)',
        [diary_code, user_id, diary_heading, diary_text, image_url, post_time]
    )