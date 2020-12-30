import sqlite3

def create(file):
    conn = sqlite3.connect(file + '.sqlite')
    cursor = conn.cursor()

    sqlstr = '''CREATE TABLE IF NOT EXITES table01 \
    (
     'date'     TEXT PRIMARY KEY NOT NULL,
     'content'  TEXT PRIMARY KEY NOT NULL
    )    
    '''
    cursor.execute(sqlstr)
    conn.commit()