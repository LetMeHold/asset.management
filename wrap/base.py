# -*- coding: utf-8 -*-

from gl import *
import pymysql.cursors

class DB:

    def __init__(self, host='localhost', port=3306, db=None, user='root', pwd='root'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, 
                charset='utf8', cursorclass=pymysql.cursors.DictCursor) 
        self.name = '%s.%d.%s' % (host,port,db)
        GL.LOG.info('数据库连接(%s)已建立' % self.name)
        self.count_success = 0
        self.count_failed = 0

    def __del__(self):
        self.conn.close()
        GL.LOG.info('数据库连接(%s)已断开' % self.name)

    def resetCount(self):
        self.count_success = 0
        self.count_failed = 0

    def getCount(self):
        return (self.count_success,self.count_failed)

    def exec(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                self.conn.commit()
                self.count_success += 1
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))

    def query(self, result, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                result.extend(cur.fetchall())
                self.count_success += 1
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))


