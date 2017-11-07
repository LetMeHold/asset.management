# -*- coding: utf-8 -*-

from gl import *
from ui import *
from wrap import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

