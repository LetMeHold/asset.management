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
        GL.LOG.info('asset.management exit')

    def connect(self):
        self.bus.connect()

    def disconnect(self):
        self.bus.disconnect()

    def relate(self):
        self.btnConn.clicked.connect(self.connect)
        self.btnDisconn.clicked.connect(self.disconnect)

