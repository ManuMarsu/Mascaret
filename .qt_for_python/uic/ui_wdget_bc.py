# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_wdget_bc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgt_tab(object):
    def setupUi(self, wdgt_tab):
        wdgt_tab.setObjectName("wdgt_tab")
        wdgt_tab.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(wdgt_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_event = QtWidgets.QComboBox(wdgt_tab)
        self.cb_event.setObjectName("cb_event")
        self.horizontalLayout.addWidget(self.cb_event)
        self.cb_law = QtWidgets.QComboBox(wdgt_tab)
        self.cb_law.setObjectName("cb_law")
        self.horizontalLayout.addWidget(self.cb_law)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fram_absweirs = QtWidgets.QFrame(wdgt_tab)
        self.fram_absweirs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram_absweirs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram_absweirs.setObjectName("fram_absweirs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fram_absweirs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lay_absweirs = QtWidgets.QHBoxLayout()
        self.lay_absweirs.setObjectName("lay_absweirs")
        self.label_7 = QtWidgets.QLabel(self.fram_absweirs)
        self.label_7.setObjectName("label_7")
        self.lay_absweirs.addWidget(self.label_7)
        self.rb_abs_z = QtWidgets.QRadioButton(self.fram_absweirs)
        self.rb_abs_z.setObjectName("rb_abs_z")
        self.lay_absweirs.addWidget(self.rb_abs_z)
        self.rb_abs_q = QtWidgets.QRadioButton(self.fram_absweirs)
        self.rb_abs_q.setObjectName("rb_abs_q")
        self.lay_absweirs.addWidget(self.rb_abs_q)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lay_absweirs.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.lay_absweirs, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.fram_absweirs)
        self.lay_graph_home = QtWidgets.QVBoxLayout()
        self.lay_graph_home.setObjectName("lay_graph_home")
        self.verticalLayout.addLayout(self.lay_graph_home)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(wdgt_tab)
        QtCore.QMetaObject.connectSlotsByName(wdgt_tab)

    def retranslateUi(self, wdgt_tab):
        _translate = QtCore.QCoreApplication.translate
        wdgt_tab.setWindowTitle(_translate("wdgt_tab", "Form"))
        self.label_7.setText(_translate("wdgt_tab", "Abscissa :  "))
        self.rb_abs_z.setText(_translate("wdgt_tab", "Downstream level"))
        self.rb_abs_q.setText(_translate("wdgt_tab", "Flowrate"))
