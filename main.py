# -*- coding: utf-8 -*-
# pyuic5.bat -o ui/ui_main.py ui/main.ui
# pyinstaller -F -w main.py -n rpstuff

from gl import *
from ui import *
from wrap import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

