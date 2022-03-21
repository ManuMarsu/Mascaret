# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\manuel.collongues\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Mascaret\ui\ui_meteo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TracerLaws(object):
    def setupUi(self, TracerLaws):
        TracerLaws.setObjectName("TracerLaws")
        TracerLaws.resize(956, 604)
        self.gridLayout_2 = QtWidgets.QGridLayout(TracerLaws)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.meteo_pages = QtWidgets.QStackedWidget(TracerLaws)
        self.meteo_pages.setEnabled(True)
        self.meteo_pages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.meteo_pages.setAutoFillBackground(False)
        self.meteo_pages.setObjectName("meteo_pages")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lst_sets = QtWidgets.QListView(self.page)
        self.lst_sets.setObjectName("lst_sets")
        self.gridLayout.addWidget(self.lst_sets, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.b_new = QtWidgets.QPushButton(self.page)
        self.b_new.setObjectName("b_new")
        self.verticalLayout_3.addWidget(self.b_new)
        self.b_edit = QtWidgets.QPushButton(self.page)
        self.b_edit.setObjectName("b_edit")
        self.verticalLayout_3.addWidget(self.b_edit)
        self.b_delete = QtWidgets.QPushButton(self.page)
        self.b_delete.setObjectName("b_delete")
        self.verticalLayout_3.addWidget(self.b_delete)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.lay_graph_home = QtWidgets.QVBoxLayout()
        self.lay_graph_home.setObjectName("lay_graph_home")
        self.gridLayout.addLayout(self.lay_graph_home, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.b_OK_page1 = QtWidgets.QDialogButtonBox(self.page)
        self.b_OK_page1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.b_OK_page1.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.b_OK_page1.setObjectName("b_OK_page1")
        self.verticalLayout_4.addWidget(self.b_OK_page1)
        self.meteo_pages.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.b_import = QtWidgets.QPushButton(self.page_2)
        self.b_import.setObjectName("b_import")
        self.verticalLayout_2.addWidget(self.b_import)
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.b_add_line = QtWidgets.QPushButton(self.page_2)
        self.b_add_line.setObjectName("b_add_line")
        self.verticalLayout_2.addWidget(self.b_add_line)
        self.b_delete_line = QtWidgets.QPushButton(self.page_2)
        self.b_delete_line.setObjectName("b_delete_line")
        self.verticalLayout_2.addWidget(self.b_delete_line)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.b_OK_page2 = QtWidgets.QDialogButtonBox(self.page_2)
        self.b_OK_page2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.b_OK_page2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.b_OK_page2.setCenterButtons(False)
        self.b_OK_page2.setObjectName("b_OK_page2")
        self.gridLayout_4.addWidget(self.b_OK_page2, 3, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_name = QtWidgets.QLineEdit(self.page_2)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout_3.addWidget(self.txt_name, 0, 1, 1, 1)
        self.label_LawWQ = QtWidgets.QLabel(self.page_2)
        self.label_LawWQ.setObjectName("label_LawWQ")
        self.gridLayout_3.addWidget(self.label_LawWQ, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.de_date = QtWidgets.QDateTimeEdit(self.page_2)
        self.de_date.setCalendarPopup(True)
        self.de_date.setObjectName("de_date")
        self.gridLayout_3.addWidget(self.de_date, 1, 1, 1, 1)
        self.cb_date = QtWidgets.QCheckBox(self.page_2)
        self.cb_date.setObjectName("cb_date")
        self.gridLayout_3.addWidget(self.cb_date, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb_sec = QtWidgets.QRadioButton(self.page_2)
        self.rb_sec.setObjectName("rb_sec")
        self.horizontalLayout_2.addWidget(self.rb_sec)
        self.rb_min = QtWidgets.QRadioButton(self.page_2)
        self.rb_min.setObjectName("rb_min")
        self.horizontalLayout_2.addWidget(self.rb_min)
        self.rb_hour = QtWidgets.QRadioButton(self.page_2)
        self.rb_hour.setObjectName("rb_hour")
        self.horizontalLayout_2.addWidget(self.rb_hour)
        self.rb_day = QtWidgets.QRadioButton(self.page_2)
        self.rb_day.setObjectName("rb_day")
        self.horizontalLayout_2.addWidget(self.rb_day)
        self.rb_date = QtWidgets.QRadioButton(self.page_2)
        self.rb_date.setObjectName("rb_date")
        self.horizontalLayout_2.addWidget(self.rb_date)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tab_sets = QtWidgets.QTableView(self.page_2)
        self.tab_sets.setEnabled(True)
        self.tab_sets.setMinimumSize(QtCore.QSize(400, 0))
        self.tab_sets.setObjectName("tab_sets")
        self.tab_sets.horizontalHeader().setDefaultSectionSize(50)
        self.tab_sets.verticalHeader().setDefaultSectionSize(22)
        self.verticalLayout.addWidget(self.tab_sets)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.lay_graph_edit = QtWidgets.QVBoxLayout()
        self.lay_graph_edit.setObjectName("lay_graph_edit")
        self.gridLayout_4.addLayout(self.lay_graph_edit, 1, 2, 1, 1)
        self.meteo_pages.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.meteo_pages, 0, 0, 1, 1)
        self.actionB_edit = QtWidgets.QAction(TracerLaws)
        self.actionB_edit.setObjectName("actionB_edit")
        self.actionComboBox_Name_law = QtWidgets.QAction(TracerLaws)
        self.actionComboBox_Name_law.setObjectName("actionComboBox_Name_law")
        self.actionB_OK_page1 = QtWidgets.QAction(TracerLaws)
        self.actionB_OK_page1.setObjectName("actionB_OK_page1")
        self.actionB_OK_page2 = QtWidgets.QAction(TracerLaws)
        self.actionB_OK_page2.setObjectName("actionB_OK_page2")
        self.actionTable_laws = QtWidgets.QAction(TracerLaws)
        self.actionTable_laws.setObjectName("actionTable_laws")
        self.actionName_edit = QtWidgets.QAction(TracerLaws)
        self.actionName_edit.setObjectName("actionName_edit")
        self.actionLaw_pages = QtWidgets.QAction(TracerLaws)
        self.actionLaw_pages.setObjectName("actionLaw_pages")
        self.actionB_new = QtWidgets.QAction(TracerLaws)
        self.actionB_new.setObjectName("actionB_new")
        self.actionB_delete = QtWidgets.QAction(TracerLaws)
        self.actionB_delete.setObjectName("actionB_delete")
        self.actionB_import = QtWidgets.QAction(TracerLaws)
        self.actionB_import.setObjectName("actionB_import")
        self.actionB_addLine = QtWidgets.QAction(TracerLaws)
        self.actionB_addLine.setObjectName("actionB_addLine")
        self.actionB_delLine = QtWidgets.QAction(TracerLaws)
        self.actionB_delLine.setObjectName("actionB_delLine")

        self.retranslateUi(TracerLaws)
        self.meteo_pages.setCurrentIndex(0)
        self.b_edit.clicked.connect(self.actionB_edit.trigger)
        self.b_new.clicked.connect(self.actionB_new.trigger)
        self.b_delete.clicked.connect(self.actionB_delete.trigger)
        self.b_import.clicked.connect(self.actionB_import.trigger)
        self.b_delete_line.clicked.connect(self.actionB_delLine.trigger)
        self.b_add_line.clicked.connect(self.actionB_addLine.trigger)
        QtCore.QMetaObject.connectSlotsByName(TracerLaws)

    def retranslateUi(self, TracerLaws):
        _translate = QtCore.QCoreApplication.translate
        TracerLaws.setWindowTitle(_translate("TracerLaws", "Meteo"))
        self.label.setText(_translate("TracerLaws", "Select Meteo Setting"))
        self.b_new.setText(_translate("TracerLaws", "New Setting"))
        self.b_edit.setText(_translate("TracerLaws", "Edit Setting"))
        self.b_delete.setText(_translate("TracerLaws", "Delete Setting"))
        self.b_import.setText(_translate("TracerLaws", "Import"))
        self.b_add_line.setText(_translate("TracerLaws", "Add Line"))
        self.b_delete_line.setText(_translate("TracerLaws", "Delete Line"))
        self.label_LawWQ.setText(_translate("TracerLaws", "Setting Name :"))
        self.cb_date.setText(_translate("TracerLaws", "Reference Date :"))
        self.rb_sec.setText(_translate("TracerLaws", "sec."))
        self.rb_min.setText(_translate("TracerLaws", "min."))
        self.rb_hour.setText(_translate("TracerLaws", "hour"))
        self.rb_day.setText(_translate("TracerLaws", "day"))
        self.rb_date.setText(_translate("TracerLaws", "date"))
        self.actionB_edit.setText(_translate("TracerLaws", "b_edit"))
        self.actionComboBox_Name_law.setText(_translate("TracerLaws", "comboBox_Name_law"))
        self.actionB_OK_page1.setText(_translate("TracerLaws", "b_OK_page1"))
        self.actionB_OK_page2.setText(_translate("TracerLaws", "b_OK_page2"))
        self.actionTable_laws.setText(_translate("TracerLaws", "Table_laws"))
        self.actionName_edit.setText(_translate("TracerLaws", "Name_edit"))
        self.actionLaw_pages.setText(_translate("TracerLaws", "Law_pages"))
        self.actionB_new.setText(_translate("TracerLaws", "b_new"))
        self.actionB_delete.setText(_translate("TracerLaws", "b_delete"))
        self.actionB_import.setText(_translate("TracerLaws", "b_import"))
        self.actionB_import.setToolTip(_translate("TracerLaws", "b_import"))
        self.actionB_addLine.setText(_translate("TracerLaws", "b_addLine"))
        self.actionB_addLine.setToolTip(_translate("TracerLaws", "b_addLine"))
        self.actionB_delLine.setText(_translate("TracerLaws", "b_delLine"))
        self.actionB_delLine.setToolTip(_translate("TracerLaws", "b_delLine"))
