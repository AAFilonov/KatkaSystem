
CREATE TABLE IF NOT EXISTS users (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password_hash VARCHAR ( 100 ) NOT NULL,
	role INTEGER DEFAULT 1
)

insert into users (username,"role",password_hash) values ('test_user','1111',3)