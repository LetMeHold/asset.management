# -*- coding: utf-8 -*-

from gl import *
from wrap.base import *
from openpyxl import Workbook
from openpyxl import load_workbook

class Business:

    def __init__(self):
        self.db = DB(db='asset.management')
        self.tol = Tools()

    def __del__(self):
        if self.db != None:
            del self.db
            self.db = None

    def getRedPrice(self, vc, typ, spec):
        sql = self.tol.queryRedPriceSql(vc, typ, spec)
        result = []
        self.db.query(result, sql)
        return result

    def getClassDiscount(self, classify):
        sql = self.tol.queryClassDiscountSql(classify)
        result = []
        self.db.query(result, sql)
        return result

    def getStandardParamSql(self, standard):
        sql = self.tol.queryStandardParamSql(standard)
        result = []
        self.db.query(result, sql)
        return result

    def loadRedPriceExcel(self):
        wb = load_workbook(filename='../../db/zjh/电子红本2017.3.14.xlsx')
        for ws in wb:
            self.db.resetCount()
            for row in ws.rows:
                if isinstance(row[0].value,int) == False:   #跳过标题行
                    continue
                if len(row) == 6:
                    vc = row[1].value.strip()
                    typ = row[2].value.strip()
                    name = row[3].value.strip()
                    spec = name[name.rfind(' '):].strip()
                    #spec = spec[len(typ):].strip()
                    unit = row[4].value.strip()
                    price = row[5].value
                    values = (vc,typ,name,spec,unit,price)
                    sql = 'insert into redprice (vc,type,name,spec,unit,price) values %s' % str(values)
                    self.db.exec(sql)
            GL.LOG.info('导入红本价(%s)成功与失败次数: %s' % (ws.title,str(self.db.getCount())))



