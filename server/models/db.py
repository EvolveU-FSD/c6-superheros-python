import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE = os.getenv('DATABASE')

def get_db():
    return sqlite3.connect(DATABASE)


def dict_from_query(cols, rows):
    # new_cols = []
    # for col in cols:
    #     new_cols.append(col[0])
    if cols:
        new_cols = [col[0] for col in cols]
        data = [{col:row[i] for i,col in enumerate(new_cols)} for row in rows]
        return data

def query(s, args=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(s,args)
    result = dict_from_query(cursor.description,cursor.fetchall())
    db.commit()
    db.close()
    return result
