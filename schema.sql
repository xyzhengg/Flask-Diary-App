-- DROP TABLE if EXISTS users;
-- DROP TABLE if EXISTS diary;
-- DROP TABLE if EXISTS entries;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password_hash TEXT NOT NULL,
    diary_code VARCHAR(8)
);

CREATE TABLE diary (
    id SERIAL PRIMARY KEY,
    diary_code VARCHAR(8) NOT NULL,
    email_1 VARCHAR(50) NOT NULL,
    email_2 VARCHAR(50)
);

CREATE TABLE entries (
    id SERIAL PRIMARY KEY,
    diary_code VARCHAR(8) NOT NULL,
    user_id INT NOT NULL,
    diary_heading VARCHAR(25),
    diary_text TEXT,
    img_url TEXT,
    fav BOOLEAN,
    post_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP(2)
    );

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    public_id TEXT,
    img_url TEXT,
    entry_id INT,
    CONSTRAINT fk_entry_images 
        FOREIGN KEY (entry_id)
        REFERENCES entries(id)
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    chat TEXT,
    user_id INTEGER,
    diary_code VARCHAR(8) NOT NULL,
    post_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP(2),
    CONSTRAINT fk_user_id 
        FOREIGN KEY (user_id) 
        REFERENCES users(id)
);