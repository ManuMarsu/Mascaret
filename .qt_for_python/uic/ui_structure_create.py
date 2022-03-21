# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_structure_create.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 204)
        Form.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_name = QtWidgets.QLineEdit(Form)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 2, 1, 1, 1)
        self.lbl_name = QtWidgets.QLabel(Form)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 2, 0, 1, 1)
        self.cb_type = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_type.sizePolicy().hasHeightForWidth())
        self.cb_type.setSizePolicy(sizePolicy)
        self.cb_type.setObjectName("cb_type")
        self.gridLayout.addWidget(self.cb_type, 1, 1, 1, 1)
        self.lbl_profil = QtWidgets.QLabel(Form)
        self.lbl_profil.setObjectName("lbl_profil")
        self.gridLayout.addWidget(self.lbl_profil, 0, 0, 1, 1)
        self.cb_profil = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_profil.sizePolicy().hasHeightForWidth())
        self.cb_profil.setSizePolicy(sizePolicy)
        self.cb_profil.setObjectName("cb_profil")
        self.gridLayout.addWidget(self.cb_profil, 0, 1, 1, 1)
        self.lbl_type = QtWidgets.QLabel(Form)
        self.lbl_type.setObjectName("lbl_type")
        self.gridLayout.addWidget(self.lbl_type, 1, 0, 1, 1)
        self.lbl_comment = QtWidgets.QLabel(Form)
        self.lbl_comment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_comment.setObjectName("lbl_comment")
        self.gridLayout.addWidget(self.lbl_comment, 3, 0, 1, 1)
        self.txt_comment = QtWidgets.QLineEdit(Form)
        self.txt_comment.setObjectName("txt_comment")
        self.gridLayout.addWidget(self.txt_comment, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.b_ok = QtWidgets.QDialogButtonBox(Form)
        self.b_ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.b_ok.setObjectName("b_ok")
        self.verticalLayout.addWidget(self.b_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Hydraulic Structure"))
        self.lbl_name.setText(_translate("Form", "Structure name"))
        self.lbl_profil.setText(_translate("Form", "Profile"))
        self.lbl_type.setText(_translate("Form", "Structure type"))
        self.lbl_comment.setText(_translate("Form", "Comments"))
