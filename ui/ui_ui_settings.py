# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(620, 473)
        Settings.setSizeGripEnabled(False)
        Settings.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_postgres = QtWidgets.QGroupBox(Settings)
        self.groupBox_postgres.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_postgres.sizePolicy().hasHeightForWidth())
        self.groupBox_postgres.setSizePolicy(sizePolicy)
        self.groupBox_postgres.setObjectName("groupBox_postgres")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_postgres)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_path_postgres = QtWidgets.QLineEdit(self.groupBox_postgres)
        self.txt_path_postgres.setObjectName("txt_path_postgres")
        self.horizontalLayout.addWidget(self.txt_path_postgres)
        self.bt_pathPostgres = QtWidgets.QPushButton(self.groupBox_postgres)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_pathPostgres.sizePolicy().hasHeightForWidth())
        self.bt_pathPostgres.setSizePolicy(sizePolicy)
        self.bt_pathPostgres.setObjectName("bt_pathPostgres")
        self.horizontalLayout.addWidget(self.bt_pathPostgres)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_postgres, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Settings)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.open_lastChbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.open_lastChbox.setChecked(True)
        self.open_lastChbox.setObjectName("open_lastChbox")
        self.verticalLayout_8.addWidget(self.open_lastChbox)
        self.open_lastChbox_schema = QtWidgets.QCheckBox(self.groupBox_3)
        self.open_lastChbox_schema.setEnabled(True)
        self.open_lastChbox_schema.setChecked(True)
        self.open_lastChbox_schema.setObjectName("open_lastChbox_schema")
        self.verticalLayout_8.addWidget(self.open_lastChbox_schema)
        self.apiChbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.apiChbox.setChecked(False)
        self.apiChbox.setObjectName("apiChbox")
        self.verticalLayout_8.addWidget(self.apiChbox)
        self.debugModeChbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.debugModeChbox.setObjectName("debugModeChbox")
        self.verticalLayout_8.addWidget(self.debugModeChbox)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.actionBt_pathPostgres = QtWidgets.QAction(Settings)
        self.actionBt_pathPostgres.setObjectName("actionBt_pathPostgres")
        self.actionTxt_path_postgres = QtWidgets.QAction(Settings)
        self.actionTxt_path_postgres.setObjectName("actionTxt_path_postgres")

        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept) # type: ignore
        self.buttonBox.rejected.connect(Settings.reject) # type: ignore
        self.bt_pathPostgres.clicked.connect(self.actionBt_pathPostgres.trigger) # type: ignore
        self.txt_path_postgres.textChanged['QString'].connect(self.actionTxt_path_postgres.trigger) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Mascaret Options"))
        self.groupBox_postgres.setTitle(_translate("Settings", "Postgres"))
        self.bt_pathPostgres.setText(_translate("Settings", "Path Postgres"))
        self.groupBox_3.setTitle(_translate("Settings", "Application"))
        self.open_lastChbox.setText(_translate("Settings", "Load last Mascaret database when starting"))
        self.open_lastChbox_schema.setText(_translate("Settings", "Load last schema when starting"))
        self.apiChbox.setText(_translate("Settings", "Use Mascaret API"))
        self.debugModeChbox.setText(_translate("Settings", "Debugging mode"))
        self.actionBt_pathPostgres.setText(_translate("Settings", "bt_pathPostgres"))
        self.actionTxt_path_postgres.setText(_translate("Settings", "txt_path_postgres"))
