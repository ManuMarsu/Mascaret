# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_structure.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 556)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b_new = QtWidgets.QPushButton(Form)
        self.b_new.setObjectName("b_new")
        self.verticalLayout_2.addWidget(self.b_new)
        self.b_edit = QtWidgets.QPushButton(Form)
        self.b_edit.setObjectName("b_edit")
        self.verticalLayout_2.addWidget(self.b_edit)
        self.b_delete = QtWidgets.QPushButton(Form)
        self.b_delete.setObjectName("b_delete")
        self.verticalLayout_2.addWidget(self.b_delete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lay_graph = QtWidgets.QVBoxLayout()
        self.lay_graph.setObjectName("lay_graph")
        self.tree_struct = QtWidgets.QTreeWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_struct.sizePolicy().hasHeightForWidth())
        self.tree_struct.setSizePolicy(sizePolicy)
        self.tree_struct.setAlternatingRowColors(True)
        self.tree_struct.setObjectName("tree_struct")
        self.lay_graph.addWidget(self.tree_struct)
        self.verticalLayout.addLayout(self.lay_graph)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hydraulic Structures"))
        self.b_new.setText(_translate("Form", "New"))
        self.b_edit.setText(_translate("Form", "Edit"))
        self.b_delete.setText(_translate("Form", "Delete"))
        self.tree_struct.headerItem().setText(0, _translate("Form", "Configuration"))
        self.tree_struct.headerItem().setText(1, _translate("Form", "Profile"))
        self.tree_struct.headerItem().setText(2, _translate("Form", "Method"))
        self.tree_struct.headerItem().setText(3, _translate("Form", "Active"))
        self.tree_struct.headerItem().setText(4, _translate("Form", "Comments"))
