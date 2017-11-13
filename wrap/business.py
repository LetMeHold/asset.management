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
        sql = self.tol.queryVcZhSql(vc)
        vcList = self.db.query(sql)
        GL.LOG.debug('vc对照: %s' % str(vcList))
        if len(vcList) == 1:
            tmp = vcList[0]['vczh']
        else:
            tmp = []
            for m in vcList:
                tmp.append(m['vczh'])
            tmp = tuple(tmp)
        sql = self.tol.queryRedPriceSql(tmp, typ, spec)
        rpList = self.db.query(sql)
        GL.LOG.debug('红本: %s' % str(rpList))
        ret = None
        if len(rpList) == 1:
            ret = rpList[0]['price']
        elif len(rpList) > 1:
            name = '%s-%s%s %s' % (typ,vc[:vc.find('/')],vcList[0]['unit'],spec)
            GL.LOG.debug('多个结果,筛选全名为: %s' % name)
            for m in rpList:
                if m['name'].lower() == name.lower():
                    ret = m['price']
        return ret

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

    def loadClassifyExcel(self):
        wb = load_workbook(filename='../../db/zjh/分类下浮标准对照表.xlsx')
        for ws in wb:
            self.db.resetCount()
            for row in ws.rows:
                if len(row) == 3:
                    clas = row[0].value
                    sn = row[1].value
                    discount = row[2].value
                    values = (clas,sn,discount)
                    sql = 'insert into classify (class,sn,discount) values %s' % str(values)
                    self.db.exec(sql)
            GL.LOG.info('导入分类下浮标准对照表(%s)成功与失败次数: %s' % (ws.title,str(self.db.getCount())))


    def loadVcMapExcel(self):
        wb = load_workbook(filename='../../db/zjh/电压等级对照表.xlsx')
        for ws in wb:
            self.db.resetCount()
            for row in ws.rows:
                if len(row) == 3:
                    vc = str(row[0].value).strip()
                    vczh = row[1].value.strip()
                    unit = row[2].value.strip()
                    values = (vc,vczh,unit)
                    sql = 'insert into vcmap (vc,vczh,unit) values %s' % str(values)
                    self.db.exec(sql)
            GL.LOG.info('导入电压等级对照表(%s)成功与失败次数: %s' % (ws.title,str(self.db.getCount())))

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


