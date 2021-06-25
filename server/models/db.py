import sqlite3
import psycopg2 as pg
from dotenv import load_dotenv
import os

load_dotenv()
DB = os.getenv('DB')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')


def get_db():
    return pg.connect(f"user={USERNAME} password={PASSWORD} dbname={DB} host={HOST}")


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
    result = None
    try:
        result = dict_from_query(cursor.description,cursor.fetchall())
    except pg.ProgrammingError:
        pass
    db.commit()
    db.close()
    return result



 