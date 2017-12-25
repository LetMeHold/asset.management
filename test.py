# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap import *

GL.LOG = getLogger('AssetLoger', 'logs', 'console.log')
bus = Business()

def test():
    vc = '0.6/1'
    ordertype = 'VV'
    orderspec = '1*1.5'
    typ = 'VV'
    spec = '1*1.5'
    #vc = '8.7/10'
    #typ = 'YJV22'
    #spec = '3*300'
    classify = '铜'
    sn = 3
    amount = 2
    rp = bus.getRedPrice(vc, typ, spec)
    #GL.LOG.info(rp)
    dis = bus.getClassDiscount(classify, sn)
    #GL.LOG.info(dis)
    val = bus.getValueRedPrice(rp, dis, amount)
    #GL.LOG.info(val)
    stuffLst = bus.getStuff(vc, sn, typ, spec, amount)
    orderno = '1111111'
    orderdate = '2017-11-17'
    bus.record(orderno,orderdate,ordertype,orderspec,vc,typ,spec,classify,sn,amount,val,stuffLst)

def loadRedPrice():
    bus.loadRedPriceExcel()

def loadVcMap():
    bus.loadVcMapExcel()

def loadClassify():
    bus.loadClassifyExcel()

def loadStuff():
    bus.loadStuffExcel()

#test()
vc = '0.6/1'
print(vc.find('/'))
print(vc[:vc.find('/')])

del bus

