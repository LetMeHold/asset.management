# -*- coding: utf-8 -*-

from gl import *
import pymysql.cursors

class Business:

    def __init__(self):
        self.conn = None

    def connect(self, host='localhost', port=3306, db=None, user='root', pwd='root'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, 
                charset='utf8', cursorclass=pymysql.cursors.DictCursor) 

    def disconnect(self):
        self.conn.close()

    def test(self, result):
        with self.conn.cursor() as cur:
            sql = 'select * from product limit 10'
            cur.execute(sql)
            result.extend(cur.fetchall())

