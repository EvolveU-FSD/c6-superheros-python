
import sqlite3
from dotenv import load_dotenv
import os
load_dotenv() 
DATABASE = os.getenv('DATABASE') or './server/superheros.sqlite'
def get_db():
    return sqlite3.connect(DATABASE)


def dict_from_cursor(cursor):
    print(cursor.__repr__())
    rows = cursor.fetchall()
    
    if cursor.description:
    
        columns = [col[0] for col in cursor.description]

        return [{column: row[i] for i,column in enumerate(columns)} for row in rows]
    else:
        return True

def query(s):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(s)
    result = dict_from_cursor(cursor)
    db.commit()
    return result
    
