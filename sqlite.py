#!/usr/bin/python

import sqlite3

# wirte appArray to sqlite
conn = sqlite3.connect('appList.db')
c = conn.cursor()
# c.execute("""CREATE TABLE appList (id integer primary key,name varchar(20) UNIQUE,time integer)""")
appArray = {20131103213338: u'Safari', 20131103213340: u'Sublime Text 2', 20131103213341: u'Terminal', 20131103213334: u'Terminal'}

c.execute("INSERT INTO appList VALUES (?,?)", appArray)
conn.commit()
conn.close()