# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\test_graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graph_test(object):
    def setupUi(self, graph_test):
        graph_test.setObjectName("graph_test")
        graph_test.resize(386, 295)
        self.gridLayout = QtWidgets.QGridLayout(graph_test)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_figure = QtWidgets.QWidget(graph_test)
        self.widget_figure.setObjectName("widget_figure")
        self.verticalLayout.addWidget(self.widget_figure)
        self.widget_toolsbar = QtWidgets.QWidget(graph_test)
        self.widget_toolsbar.setObjectName("widget_toolsbar")
        self.verticalLayout.addWidget(self.widget_toolsbar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(graph_test)
        QtCore.QMetaObject.connectSlotsByName(graph_test)

    def retranslateUi(self, graph_test):
        _translate = QtCore.QCoreApplication.translate
        graph_test.setWindowTitle(_translate("graph_test", "graph test"))
