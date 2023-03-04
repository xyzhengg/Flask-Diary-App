import db

def add_entry(diary_code, user_id, diary_heading, diary_text, img_url):
    db.sql_write(
        'INSERT INTO entries (diary_code, user_id, diary_heading, diary_text, img_url) VALUES (%s, %s, %s, %s, %s)',
        [diary_code, user_id, diary_heading, diary_text, img_url]
    )

def get_all_posts(diary_id):
    data = db.sql_select(
        'SELECT * FROM entries WHERE diary_code = %s ORDER BY post_time DESC', [diary_id]
    ) 
    return data