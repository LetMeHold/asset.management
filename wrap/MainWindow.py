# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap.business import Business
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        GL.LOG = getLogger('AssetLoger', 'logs/console.log')
        GL.LOG.info('asset.management start')
        self.relate()
        self.bus = Business()

    def closeEvent(self, event):
        self.disconnect()
        GL.LOG.info('asset.management exit')

    def connect(self):
        try:
            self.bus.connect(db='asset.management')
            GL.LOG.info('数据库连接已建立')
        except:
            GL.LOG.error('建立数据库连接失败\n' + traceback.format_exc())

    def disconnect(self):
        try:
            self.bus.disconnect()
            GL.LOG.info('数据库连接已断开')
        except: 
            GL.LOG.error('断开数据库连接失败\n' + traceback.format_exc())

    def test(self):
        try:
            result = []
            self.bus.test(result)
            for r in result:
                GL.LOG.info(r)
        except: 
            GL.LOG.error('执行数据库操作失败\n' + traceback.format_exc())

    def relate(self):
        self.btnConn.clicked.connect(self.connect)
        self.btnDisconn.clicked.connect(self.disconnect)
        self.btnTest.clicked.connect(self.test)

