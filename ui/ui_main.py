# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editIP = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editIP.sizePolicy().hasHeightForWidth())
        self.editIP.setSizePolicy(sizePolicy)
        self.editIP.setMaximumSize(QtCore.QSize(150, 16777215))
        self.editIP.setObjectName("editIP")
        self.horizontalLayout_3.addWidget(self.editIP)
        self.editPort = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editPort.sizePolicy().hasHeightForWidth())
        self.editPort.setSizePolicy(sizePolicy)
        self.editPort.setMaximumSize(QtCore.QSize(75, 16777215))
        self.editPort.setObjectName("editPort")
        self.horizontalLayout_3.addWidget(self.editPort)
        self.btnConn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConn.sizePolicy().hasHeightForWidth())
        self.btnConn.setSizePolicy(sizePolicy)
        self.btnConn.setObjectName("btnConn")
        self.horizontalLayout_3.addWidget(self.btnConn)
        self.btnDisconn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisconn.sizePolicy().hasHeightForWidth())
        self.btnDisconn.setSizePolicy(sizePolicy)
        self.btnDisconn.setObjectName("btnDisconn")
        self.horizontalLayout_3.addWidget(self.btnDisconn)
        self.labConn = QtWidgets.QLabel(self.centralwidget)
        self.labConn.setMinimumSize(QtCore.QSize(200, 0))
        self.labConn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labConn.setObjectName("labConn")
        self.horizontalLayout_3.addWidget(self.labConn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTest.sizePolicy().hasHeightForWidth())
        self.btnTest.setSizePolicy(sizePolicy)
        self.btnTest.setObjectName("btnTest")
        self.horizontalLayout_3.addWidget(self.btnTest)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabVal = QtWidgets.QWidget()
        self.tabVal.setObjectName("tabVal")
        self.layoutWidget = QtWidgets.QWidget(self.tabVal)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 891, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cmbSn = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSn.sizePolicy().hasHeightForWidth())
        self.cmbSn.setSizePolicy(sizePolicy)
        self.cmbSn.setMinimumSize(QtCore.QSize(200, 25))
        self.cmbSn.setObjectName("cmbSn")
        self.gridLayout.addWidget(self.cmbSn, 8, 1, 1, 1)
        self.sbAmount = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbAmount.sizePolicy().hasHeightForWidth())
        self.sbAmount.setSizePolicy(sizePolicy)
        self.sbAmount.setMinimumSize(QtCore.QSize(0, 25))
        self.sbAmount.setObjectName("sbAmount")
        self.gridLayout.addWidget(self.sbAmount, 9, 1, 1, 1)
        self.edtVc = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtVc.sizePolicy().hasHeightForWidth())
        self.edtVc.setSizePolicy(sizePolicy)
        self.edtVc.setMinimumSize(QtCore.QSize(200, 25))
        self.edtVc.setObjectName("edtVc")
        self.gridLayout.addWidget(self.edtVc, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.cmbClass = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbClass.sizePolicy().hasHeightForWidth())
        self.cmbClass.setSizePolicy(sizePolicy)
        self.cmbClass.setMinimumSize(QtCore.QSize(200, 25))
        self.cmbClass.setObjectName("cmbClass")
        self.gridLayout.addWidget(self.cmbClass, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.edtSpec = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtSpec.sizePolicy().hasHeightForWidth())
        self.edtSpec.setSizePolicy(sizePolicy)
        self.edtSpec.setMinimumSize(QtCore.QSize(200, 25))
        self.edtSpec.setObjectName("edtSpec")
        self.gridLayout.addWidget(self.edtSpec, 5, 1, 1, 1)
        self.edtTyp = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtTyp.sizePolicy().hasHeightForWidth())
        self.edtTyp.setSizePolicy(sizePolicy)
        self.edtTyp.setMinimumSize(QtCore.QSize(200, 25))
        self.edtTyp.setObjectName("edtTyp")
        self.gridLayout.addWidget(self.edtTyp, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.edtInfo = QtWidgets.QTextEdit(self.layoutWidget)
        self.edtInfo.setObjectName("edtInfo")
        self.gridLayout.addWidget(self.edtInfo, 0, 2, 11, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.edtDate = QtWidgets.QDateEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtDate.sizePolicy().hasHeightForWidth())
        self.edtDate.setSizePolicy(sizePolicy)
        self.edtDate.setMinimumSize(QtCore.QSize(200, 25))
        self.edtDate.setObjectName("edtDate")
        self.gridLayout.addWidget(self.edtDate, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.edtOrderSpec = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrderSpec.sizePolicy().hasHeightForWidth())
        self.edtOrderSpec.setSizePolicy(sizePolicy)
        self.edtOrderSpec.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrderSpec.setObjectName("edtOrderSpec")
        self.gridLayout.addWidget(self.edtOrderSpec, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.edtOrderTyp = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrderTyp.sizePolicy().hasHeightForWidth())
        self.edtOrderTyp.setSizePolicy(sizePolicy)
        self.edtOrderTyp.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrderTyp.setObjectName("edtOrderTyp")
        self.gridLayout.addWidget(self.edtOrderTyp, 2, 1, 1, 1)
        self.edtOrder = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtOrder.sizePolicy().hasHeightForWidth())
        self.edtOrder.setSizePolicy(sizePolicy)
        self.edtOrder.setMinimumSize(QtCore.QSize(200, 25))
        self.edtOrder.setObjectName("edtOrder")
        self.gridLayout.addWidget(self.edtOrder, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setMinimumSize(QtCore.QSize(100, 25))
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 11, 2, 1, 1)
        self.btnCount = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCount.sizePolicy().hasHeightForWidth())
        self.btnCount.setSizePolicy(sizePolicy)
        self.btnCount.setMinimumSize(QtCore.QSize(100, 25))
        self.btnCount.setObjectName("btnCount")
        self.gridLayout.addWidget(self.btnCount, 10, 1, 1, 1)
        self.layoutWidget.raise_()
        self.edtInfo.raise_()
        self.tabWidget.addTab(self.tabVal, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 26))
        self.menubar.setObjectName("menubar")
        self.menuAsset = QtWidgets.QMenu(self.menubar)
        self.menuAsset.setObjectName("menuAsset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManagement = QtWidgets.QAction(MainWindow)
        self.actionManagement.setObjectName("actionManagement")
        self.menuAsset.addAction(self.actionManagement)
        self.menubar.addAction(self.menuAsset.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnConn, self.btnDisconn)
        MainWindow.setTabOrder(self.btnDisconn, self.editIP)
        MainWindow.setTabOrder(self.editIP, self.editPort)
        MainWindow.setTabOrder(self.editPort, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "asset.management"))
        self.editIP.setText(_translate("MainWindow", "127.0.0.1"))
        self.editPort.setText(_translate("MainWindow", "3306"))
        self.btnConn.setText(_translate("MainWindow", "connect"))
        self.btnDisconn.setText(_translate("MainWindow", "disconnect"))
        self.labConn.setText(_translate("MainWindow", "disconnect"))
        self.btnTest.setText(_translate("MainWindow", "test"))
        self.label.setText(_translate("MainWindow", "电压等级"))
        self.label_6.setText(_translate("MainWindow", "数量"))
        self.label_5.setText(_translate("MainWindow", "分类标准"))
        self.label_4.setText(_translate("MainWindow", "分类"))
        self.label_8.setText(_translate("MainWindow", "下单型号"))
        self.label_7.setText(_translate("MainWindow", "单号"))
        self.label_10.setText(_translate("MainWindow", "日期"))
        self.label_3.setText(_translate("MainWindow", "实际规格"))
        self.label_2.setText(_translate("MainWindow", "实际型号"))
        self.label_9.setText(_translate("MainWindow", "下单规格"))
        self.btnClear.setText(_translate("MainWindow", "清空"))
        self.btnCount.setText(_translate("MainWindow", "确认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVal), _translate("MainWindow", "redprice"))
        self.pushButton.setText(_translate("MainWindow", "1111"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_2.setText(_translate("MainWindow", "22222"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuAsset.setTitle(_translate("MainWindow", "asset"))
        self.actionManagement.setText(_translate("MainWindow", "management"))

