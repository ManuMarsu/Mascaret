# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\scores\ui_distib_score.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_autre(object):
    def setupUi(self, autre):
        autre.setObjectName("autre")
        autre.resize(782, 720)
        self.gridLayout = QtWidgets.QGridLayout(autre)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.taberr = QtWidgets.QTabWidget(autre)
        self.taberr.setObjectName("taberr")
        self.err = QtWidgets.QWidget()
        self.err.setObjectName("err")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.err)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_dist = QtWidgets.QTableWidget(self.err)
        self.table_dist.setObjectName("table_dist")
        self.table_dist.setColumnCount(0)
        self.table_dist.setRowCount(0)
        self.table_dist.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout_2.addWidget(self.table_dist, 0, 0, 1, 1)
        self.taberr.addTab(self.err, "")
        self.err_abs = QtWidgets.QWidget()
        self.err_abs.setObjectName("err_abs")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.err_abs)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.table_dist_abs = QtWidgets.QTableWidget(self.err_abs)
        self.table_dist_abs.setTextElideMode(QtCore.Qt.ElideRight)
        self.table_dist_abs.setObjectName("table_dist_abs")
        self.table_dist_abs.setColumnCount(0)
        self.table_dist_abs.setRowCount(0)
        self.table_dist_abs.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout_3.addWidget(self.table_dist_abs, 0, 0, 1, 1)
        self.taberr.addTab(self.err_abs, "")
        self.verticalLayout.addWidget(self.taberr)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_export_csv = QtWidgets.QPushButton(autre)
        self.bt_export_csv.setObjectName("bt_export_csv")
        self.horizontalLayout_2.addWidget(self.bt_export_csv)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(autre)
        self.taberr.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(autre)

    def retranslateUi(self, autre):
        _translate = QtCore.QCoreApplication.translate
        autre.setWindowTitle(_translate("autre", "Form"))
        self.taberr.setTabText(self.taberr.indexOf(self.err), _translate("autre", "Error quantiles"))
        self.taberr.setTabText(self.taberr.indexOf(self.err_abs), _translate("autre", "Absolute error quantiles"))
        self.bt_export_csv.setText(_translate("autre", "Export CSV"))