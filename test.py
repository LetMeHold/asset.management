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
classify = '铜'
standard = 3
amount = 2
rp = bus.getRedPrice(vc, typ, spec)
GL.LOG.info(rp)
dis = bus.getClassDiscount(classify, standard)
GL.LOG.info(dis)
val = bus.getValueRedPrice(rp, dis, amount)
GL.LOG.info(val)

def loadRedPrice():
    bus.loadRedPriceExcel()

def loadVcMap():
    bus.loadVcMapExcel()

def loadClassify():
    bus.loadClassifyExcel()

del bus

