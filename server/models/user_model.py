from werkzeug.security import generate_password_hash, check_password_hash
from models.db import query

def find_by_username(username):
    user = query('SELECT * from "user"   where username=%s',(username,))
    if user:
        return user
    return None

def authenticate(username, password):
    user = query('SELECT * from "user" WHERE username=%s',(username,))[0]
    print('password',   password)    
    if check_password_hash(user['password'],password):
        return user
    return None

def create(username,password):
    print(username,password)
    hashed_password = generate_password_hash(password)
    query('INSERT INTO "user" (username, password) VALUES (%s,%s)',(username,hashed_password))
    created_user = query('SELECT * from "user" WHERE username=%s',(username,))[0]
    return created_user
def find_by_id(id):
    user = query('SELECT * from "user" where id=%s',(id,))
    if user:
        return user[0]
    return None


