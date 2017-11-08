# -*- coding: utf-8 -*-

from gl import *
from wrap.base import DB
from openpyxl import Workbook
from openpyxl import load_workbook

class Business:

    def __init__(self):
        self.db = DB(db='asset.management')

    def __del__(self):
        if self.db != None:
            del self.db
            self.db = None

    def loadRedPriceExcel(self, sheet):
        wb = load_workbook(filename='../../db/zjh/河南虹峰电缆股份有限公司-电子红本新本2016.11.17.xlsx')
        for ws in wb:
            if sheet != ws.title:
                continue
            self.db.resetCount()
            for row in ws.rows:
                if len(row)==6 and row[1].value==ws.title:
                    vc = row[1].value.strip()
                    typ = row[2].value.strip()
                    spec = row[3].value.strip()
                    spec = spec[len(typ):].strip()
                    unit = row[4].value.strip()
                    price = row[5].value
                    values = (vc,typ,spec,unit,price)
                    sql = 'insert into redprice (vc,type,spec,unit,price) values %s' % str(values)
                    self.db.exec(sql)
            GL.LOG.info('导入红本价(%s)成功与失败次数: %s' % (ws.title,str(self.db.getCount())))



