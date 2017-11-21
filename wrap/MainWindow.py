# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap.business import Business
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./i.jpg'))
        GL.LOG = getLogger('AssetLoger', 'logs', 'console.log')
        GL.LOG.info('asset.management start')
        self.relate()
        self.initdata()
        self.bus = None
        self.connect()

    def closeEvent(self, event):
        self.disconnect()
        GL.LOG.info('asset.management exit')

    def connect(self):
        if self.bus != None:
            del self.bus
        self.bus = Business()
        self.labConn.setStyleSheet('color:green')
        self.labConn.setText('已连接')

    def disconnect(self):
        if self.bus != None:
            del self.bus
            self.bus = None
            self.labConn.setStyleSheet('color:red')
            self.labConn.setText('已断开')

    def outRedPrice(self):
        if self.bus == None:
            return
        orderno = self.edtOrder.text()
        orderdate = self.edtDate.date().toString('yyyy-MM-dd')
        ordertyp = self.edtOrderTyp.text()
        orderspec = self.edtOrderSpec.text()
        typ = self.edtTyp.text()
        spec = self.edtSpec.text()
        vc = self.edtVc.text()
        clas = self.cmbClass.currentText()
        sn = int(self.cmbSn.currentText())
        amount = self.sbAmount.value()
        rp = self.bus.getRedPrice(vc, typ, spec)
        if rp == False:
            self.showErr()
            return
        dis = self.bus.getClassDiscount(clas, sn)
        if dis == False:
            self.showErr()
            return
        val = self.bus.getValueRedPrice(rp, dis, amount)
        stuffLst = self.bus.getStuff(vc, sn, typ, spec, amount)
        if stuffLst == False:
            self.showErr()
            return
        self.bus.record(orderno,orderdate,ordertyp,orderspec,vc,typ,spec,clas,sn,amount,val,stuffLst)
        tmp = {}
        i = 1
        for f in stuffLst:
            if f > 0.0:
                name = self.bus.getStuffNameById(i)
                tmp[name] = f
            i += 1

        self.edtInfo.append('%s %s %s %s\n%s %s %s %s%d %d\n产值:%f 用料:%s\n已记录\n' \
                % (orderno,orderdate,ordertyp,orderspec,typ,spec,vc,clas,sn,amount,rp,str(tmp)))

    def typChanged(self, data):
        self.edtTyp.setText(data)

    def specChanged(self, data):
        self.edtSpec.setText(data)

    def clearInfo(self):
        self.edtInfo.clear()

    def recordColumn(self):
        need = ['orderno','orderdate','ordertype','orderspec','vc','amount','outprice']
        tmp = []
        for dct in self.record:
            for k,v in dct.items():
                if k.find('sid')!=-1 and v>0.0:
                    if k not in tmp:
                        tmp.append(k)
        need.extend(sorted(tmp))
        self.countindex = need.index('outprice')
        return need

    def queryRecord(self):
        if self.bus == None:
            return
        startdate = self.edtStartDate.date().toString('yyyy-MM-dd')
        enddate = self.edtEndDate.date().toString('yyyy-MM-dd')
        orderno = self.edtQryOrder.text()
        typ = self.edtQryTyp.text()
        spec = self.edtQrySpec.text()
        self.record = self.bus.getRecord(startdate, enddate, orderno, typ, spec)
        self.recordmap = self.bus.getRecordColumn()
        self.recordcol = self.recordColumn()
        self.recordhead = []    #表头
        for l in self.recordcol:
            self.recordhead.append(self.recordmap[l])
        self.fillRecordTable()

    def fillRecordTable(self):
        self.twData.clear()
        self.twData.setColumnCount(len(self.recordhead))
        self.twData.setRowCount(len(self.record))
        self.twData.setHorizontalHeaderLabels(self.recordhead)
        self.twData.setVisible(False)
        self.filldata = []
        for r in range(0,self.twData.rowCount()):
            tmp = []
            for c in range(0,self.twData.columnCount()):
                t = self.record[r][self.recordcol[c]]
                tmp.append(t)
                it = QTableWidgetItem(str(t))
                self.twData.setItem(r,c,it)
            self.filldata.append(tmp)
        self.twData.setRowCount(self.twData.rowCount()+1)
        countrow = self.twData.rowCount()-1
        it = QTableWidgetItem('合计')
        self.twData.setItem(countrow,0,it)
        for c in range(self.countindex,self.twData.columnCount()):
            v = 0.0
            for l in self.filldata:
                v += l[c]
            it = QTableWidgetItem('%.3f' % v)
            self.twData.setItem(countrow,c,it)
        self.twData.setVisible(True)
        return

    def relate(self):
        self.btnConn.clicked.connect(self.connect)
        self.btnDisconn.clicked.connect(self.disconnect)
        self.btnCount.clicked.connect(self.outRedPrice)
        self.btnClear.clicked.connect(self.clearInfo)
        self.edtOrderTyp.textChanged.connect(self.typChanged)
        self.edtOrderSpec.textChanged.connect(self.specChanged)
        self.btnQuery.clicked.connect(self.queryRecord)

    def initdata(self):
        #self.edtOrder.setText('00000000')
        now = QDate.currentDate()
        self.edtDate.setDate(now)
        self.edtStartDate.setDate(now)
        self.edtEndDate.setDate(now)
        #self.edtOrderTyp.setText('VV')
        #self.edtOrderSpec.setText('1*1.5')
        #self.edtVc.setText('0.6/1')
        self.cmbClass.addItem('铜')
        self.cmbClass.addItem('铝')
        self.cmbClass.selectIndex = 0
        self.cmbSn.addItem('1')
        self.cmbSn.addItem('2')
        self.cmbSn.addItem('3')
        self.cmbSn.addItem('4')
        self.cmbSn.selectIndex = 0
        self.sbAmount.setRange(1,65535)
        self.labConn.setStyleSheet('color:red')
        self.labConn.setText('已断开')
        self.edtInfo.setReadOnly(True)
        self.edtInfo.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)    #不自动换行
        self.twData.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.twData.verticalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    def showErr(self):
        self.statusbar.showMessage(GL.ERR, 5000)

