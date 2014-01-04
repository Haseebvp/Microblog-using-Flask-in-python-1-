import sqlite3 as Lite
con=Lite.connect('1.db')
cur=con.cursor()
cur.execute('drop table if exists A')
cur.execute('create table A(id serial,title text,post text)')
con.commit()
