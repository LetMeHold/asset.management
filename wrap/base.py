# -*- coding: utf-8 -*-

from gl import *
import pymysql.cursors

class Tools:

    def getVCName(self, vcNum):
        if vcNum==1 or vcNum==10:
            return ('架空绝缘电缆',)
        elif vcNum == 0.6:
            return ('低压电力电缆',)
        elif vcNum < 0.6:
            return ('电线','控制电缆','计算机电缆')
        elif vcNum > 0.6:
            return ('中压电力电缆',)
        else:
            return None

    def queryRedPriceSql(self, vcNum, typ, spec):
        vcName = self.getVCName(vcNum)
        if vcName == None:
            return None
        return 'select price from redprice where vc in %s and type="%s" and spec="%s"'\
                % (str(vcName),typ,spec)

    def queryClassDiscountSql(self, classify):
        return 'select discount from classify where name ="%s"' % classify

    def queryStandardParamSql(self, standard):
        return 'select param from standard where name ="%s"' % standard

class DB:

    def __init__(self, host='localhost', port=3306, db=None, user='root', pwd='root'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, 
                charset='utf8', cursorclass=pymysql.cursors.DictCursor) 
        self.name = '%s.%d.%s' % (host,port,db)
        GL.LOG.info('数据库连接(%s)已建立' % self.name)
        self.count_success = 0
        self.count_failed = 0

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


