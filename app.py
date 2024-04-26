import sqlite3

from flask import Flask


app = Flask(__name__)

conn = sqlite3.connect('mziuri.db')
curs = conect.cursor()

cursor.excute("""
create table if not exists users
(id integer primary key,
first_name text,
last_name text,
age integer,
university text,
faculty text,
is_active_or_no text,
when_started integer,
when_ended integer
""")
conect.commit

curs.execute("INSERT INTO users VALUES ('name1', 'last_name1', 'TSU', 'activate', 'english', '2000', '2005')")
curs.execute("INSERT INTO users VALUES ('name2', 'last_name2', 'TSU', 'no activate', 'english', '2000', '2005')")
curs.execute("INSERT INTO users VALUES ('name3', 'last_name3', 'TSU', 'activate', 'english', '2000', '2005')")

if __name__ == '__main__':
    app.run(debug=True)
