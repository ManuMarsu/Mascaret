# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_curve_selector_slide.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(569, 113)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_run = QtWidgets.QComboBox(Form)
        self.cb_run.setObjectName("cb_run")
        self.horizontalLayout.addWidget(self.cb_run)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cb_scen = QtWidgets.QComboBox(Form)
        self.cb_scen.setObjectName("cb_scen")
        self.horizontalLayout.addWidget(self.cb_scen)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cb_graph = QtWidgets.QComboBox(Form)
        self.cb_graph.setObjectName("cb_graph")
        self.horizontalLayout.addWidget(self.cb_graph)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_com = QtWidgets.QLabel(Form)
        self.label_com.setObjectName("label_com")
        self.horizontalLayout_6.addWidget(self.label_com)
        self.lbl_com = QtWidgets.QLabel(Form)
        self.lbl_com.setObjectName("lbl_com")
        self.horizontalLayout_6.addWidget(self.lbl_com)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sld_det = QtWidgets.QSlider(Form)
        self.sld_det.setOrientation(QtCore.Qt.Horizontal)
        self.sld_det.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sld_det.setObjectName("sld_det")
        self.horizontalLayout_2.addWidget(self.sld_det)
        self.cb_det = QtWidgets.QComboBox(Form)
        self.cb_det.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cb_det.setObjectName("cb_det")
        self.horizontalLayout_2.addWidget(self.cb_det)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.sld_det.valueChanged['int'].connect(self.cb_det.setCurrentIndex) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Run"))
        self.label_2.setText(_translate("Form", "Scenario"))
        self.label_3.setText(_translate("Form", "Chart"))
        self.label_com.setText(_translate("Form", "Comments :"))
        self.lbl_com.setText(_translate("Form", "TextLabel"))
