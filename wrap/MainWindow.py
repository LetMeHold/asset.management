# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap.business import Business
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        GL.LOG = getLogger('AssetLoger', 'logs', 'console.log')
        GL.LOG.info('asset.management start')
        self.relate()
        self.initdata()
        self.bus = None

    def closeEvent(self, event):
        self.disconnect()
        GL.LOG.info('asset.management exit')

    def connect(self):
        if self.bus != None:
            del self.bus
        self.bus = Business()

    def disconnect(self):
        if self.bus != None:
            del self.bus
            self.bus = None

    def outRedPrice(self):
        if self.bus == None:
            return
        vc = self.edtVc.text()
        typ = self.edtTyp.text()
        spec = self.edtSpec.text()
        clas = self.cmbClass.currentText()
        sn = int(self.cmbSn.currentText())
        amount = self.sbAmount.value()
        rp = self.bus.getRedPrice(vc, typ, spec)
        dis = self.bus.getClassDiscount(clas, sn)
        val = self.bus.getValueRedPrice(rp, dis, amount)
        #tmp = '%s %s %s %s %d %d' % (vc,typ,spec,clas,sn,amount)
        #GL.LOG.info(tmp)
        self.edtResult.setText(str(val))

    def test(self):
        pass

    def relate(self):
        self.btnConn.clicked.connect(self.connect)
        self.btnDisconn.clicked.connect(self.disconnect)
        self.btnTest.clicked.connect(self.test)
        self.btnCount.clicked.connect(self.outRedPrice)

    def initdata(self):
        self.edtVc.setText('0.6/1')
        self.edtTyp.setText('VV')
        self.edtSpec.setText('1*1.5')
        self.cmbClass.addItem('铜')
        self.cmbClass.addItem('铝')
        self.cmbClass.selectIndex = 0
        self.cmbSn.addItem('1')
        self.cmbSn.addItem('2')
        self.cmbSn.addItem('3')
        self.cmbSn.addItem('4')
        self.cmbSn.selectIndex = 0
        self.sbAmount.setRange(1,65535)
        self.edtResult.setReadOnly(True)

