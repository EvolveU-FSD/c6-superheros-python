
import sqlite3
from dotenv import load_dotenv
import os
import psycopg2
load_dotenv() 
DATABASE = os.getenv('DATABASE')
def get_db():
    return psycopg2.connect(host="localhost",database="c6superheros",user="postgres",password="password")

    return sqlite3.connect(DATABASE)


def dict_from_cursor(cursor):

    
    if cursor.description:
        rows = cursor.fetchall()
    
        columns = [col[0] for col in cursor.description]

        # data = []
        # for row in rows:
        #     dataRow = {}
        #     for index,column in enumerate(columns):
        #         dataRow[column] = row[index]
        #     data.append(dataRow)
        # return data

        return [{column:row[index] for index,column in enumerate(columns)} for row in rows]

    else:
        return True

def query(s,values=()):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(s,values)
    result = dict_from_cursor(cursor)
    db.commit()
    db.close()
    return result


    
