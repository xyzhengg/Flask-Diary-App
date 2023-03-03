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
    fav BOOLEAN,
    post_time TIMESTAMP
    );