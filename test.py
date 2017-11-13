# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap import *

GL.LOG = getLogger('AssetLoger', 'logs', 'console.log')
bus = Business()

vc = '0.6/1'
typ = 'VV'
spec = '1*1.5'
#vc = '8.7/10'
#typ = 'YJV22'
#spec = '3*300'
classify = '铝'
standard = '标3'
amount = 2
ret = bus.getRedPrice(vc, typ, spec)
GL.LOG.info(ret)

def outValue(vc, typ, spec, classify, standard, amount):
    ret = bus.getRedPrice(vc, typ, spec)
    #单价
    price = ret[0]['price']
    ret = bus.getClassDiscount(classify)
    #下浮
    discount = ret[0]['discount']
    ret = bus.getStandardParamSql(standard)
    #标准基数
    param = ret[0]['param']
    GL.LOG.info('查出: \n\t单价: %f\n\t下浮: %f\n\t标准: %d\n\t数量: %d' % (price,discount,param,amount))
    value = price * amount
    for i in range(0,param):
        value *= discount
    return value

def outValTest():
    vc = 0.5
    tpy = 'BV'
    spec = '0.75'
    classify = '铝'
    standard = '标3'
    amount = 2

    GL.LOG.info('输入: 电压(%f) 型号(%s) 规格(%s) 分类(%s) 标准(%s) 数量(%d)' % \
                (vc,tpy,spec,classify,standard,amount))
    val = outValue(vc, tpy, spec, classify, standard, amount)
    GL.LOG.info('计算出产值红本价: %f' % val)

def loadRedPrice():
    bus.loadRedPriceExcel()

def loadVcMap():
    bus.loadVcMapExcel()

def loadClassify():
    bus.loadClassifyExcel()



del bus

