from models.db import query
from werkzeug.security import check_password_hash, generate_password_hash


def find_all():
  
    return query('select * from user')

def find_by_id(id):
    try:
        return query(f'select * from user where id={id}')[0]
    except Exception as e:
        return {"error":e}

def find_by_username(username):
    try:
        return query(f'select * from user where username=\'{username}\'')[0]
    except Exception as e:
        return None

def authenticate(username,password):
    try:
        user = query(f'select * from user where username=\'{username}\'')[0]
        
        if check_password_hash(user['password'],password):
            print('success')
            return user
        return None
        
    except Exception as e:
        return {"error":e}

def create(user_to_create): 
    print(user_to_create)
    insert_sql = "insert into user (username, password) values (?,?)" 
    args = (user_to_create['username'],generate_password_hash(user_to_create['password']))
    query(insert_sql, args)
    new_user = query('select * from user where username=?',[user_to_create['username']]) [0]  
    
    return new_user

def update(id,user_to_update):
    
    update_sql = f"update user set username=?, password=? where id={id}" 
    args = (user_to_update['username'],user_to_update['password'])
    
    return query(update_sql, args)


def delete_user(id):
    delete_sql = f"delete from user where id={id}"
    query(delete_sql)

