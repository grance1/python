#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

con = MySQLdb.connect(host='127.0.0.1',  user='root', passwd='123', db='test')
cur = con.cursor()
cur.execute("SELECT * FROM test2")
rs = cur.fetchall()
for r in rs:
    print r
cur.close()
con.close()