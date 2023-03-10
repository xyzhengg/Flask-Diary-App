import db

def add_chat(chat, user_id, diary_id):
    result = db.sql_write_return(
        'INSERT INTO messages (chat, user_id, diary_code) VALUES (%s, %s, %s) RETURNING post_time',
        [chat, user_id, diary_id]
    )
    return result

def get_all_chats(diary_id):
    data = db.sql_select(
        'SELECT * FROM messages WHERE diary_code = %s ORDER BY post_time ASC', [diary_id]
    ) 
    return data

