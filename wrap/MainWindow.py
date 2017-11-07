# -*- coding: utf-8 -*-

from gl import *
from ui import *
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        GL.LOG = getLogger('AssetLoger', 'logs/console.log')
        GL.LOG.info('asset.management start')

    def closeEvent(self, event):
        GL.LOG.info('asset.management quit')

