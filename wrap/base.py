# -*- coding: utf-8 -*-

from gl import *
import pymysql.cursors

class Tools:

    def queryVcZhSql(self, vc):
        return 'select vc,vczh,unit from vcmap where vc="%s"' % vc

    def queryRedPriceSql(self, vc, typ, spec):
        if isinstance(vc, tuple):
            return 'select vc,name,price from redprice where vc in %s and type="%s" and spec="%s"'\
                % (str(vc),typ,spec)
        else:
            return 'select vc,name,price from redprice where vc="%s" and type="%s" and spec="%s"'\
                % (vc,typ,spec)

    def queryClassDiscountSql(self, classify, sn):
        return 'select discount from classify where class="%s" and sn<=%d' % (classify,sn)

    def queryStuffSql(self, vc, sn, typ, spec):
        return 'select * from stuff where vc="%s" and sn=%d and type="%s" and spec="%s"' % (vc,sn,typ,spec)


class DB:

    def __init__(self, host='localhost', port=3306, db=None, user='root', pwd='root'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, 
                charset='utf8', cursorclass=pymysql.cursors.DictCursor) 
        self.name = '%s.%d.%s' % (host,port,db)
        GL.LOG.info('数据库连接(%s)已建立' % self.name)
        self.count_success = 0
        self.count_failed = 0
        ret = self.query('select count(id) from stuffid')
        GL.maxStuffid = ret[0]['count(id)']
        self.resetCount()

    def __del__(self):
        GL.LOG.info('数据库连接(%s)已断开' % self.name)
        self.conn.close()

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
                return True
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))
            return False

    def query(self, sql):
        result = []
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                result.extend(cur.fetchall())
                self.count_success += 1
                return result
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))
            return False


