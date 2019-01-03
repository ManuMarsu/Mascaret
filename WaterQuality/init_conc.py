# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Mascaret
Description          : Pre and Postprocessing for Mascaret for QGIS
Date                 : December,2017
copyright            : (C) 2017 by Artelia
email                :
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.uic import *

if int(qVersion()[0]) < 5:  # qt4
    from qgis.PyQt.QtGui import *
else:  # qt5
    from qgis.PyQt.QtGui import QStandardItemModel, QStandardItem, QKeySequence
    from qgis.PyQt.QtWidgets import *
import os
from qgis.core import *
from qgis.utils import *
from qgis.gui import *

from .graph_WQ import GraphInitConc
from .table_WQ import table_WQ


class init_conc_dialog(QDialog):
    def __init__(self, obj, id, name):
        QDialog.__init__(self)
        self.paramTr = obj
        self.mgis = obj.mgis
        self.ui = obj.ui
        self.mdb = self.mgis.mdb
        self.tbwq = table_WQ(self.mgis, self.mdb)
        self.cur_wq_mod = self.tbwq.dico_mod_wq[obj.type]
        self.cur_wq_law = id
        self.cur_wq_law_name = name
        self.filling_tab = False

        self.ui = loadUi(os.path.join(self.mgis.masplugPath, 'ui/ui_init_conc.ui'), self)

        self.ui.tab_laws.sCut_del = QShortcut(QKeySequence("Del"), self)
        self.ui.tab_laws.sCut_del.activated.connect(self.shortCut_row_del)

        styledItemDelegate = QStyledItemDelegate()
        styledItemDelegate.setItemEditorFactory(ItemEditorFactory())
        self.ui.tab_laws.setItemDelegate(styledItemDelegate)

        self.ui.actionB_import.triggered.connect(self.import_csv)
        self.ui.actionB_addLine.triggered.connect(self.new_val)
        self.ui.actionB_delLine.triggered.connect(self.delete_val)
        self.ui.b_OK_page2.accepted.connect(self.acceptPage2)
        self.ui.b_OK_page2.rejected.connect(self.rejectPage2)
        self.ui.cb_bief.currentIndexChanged[int].connect(self.change_bief)

        self.initUI()

    def initUI(self):
        self.ui.LawWQ.setText(self.cur_wq_law_name)
        self.graph_edit = GraphInitConc(self.mgis, self.ui.lay_graph_edit)
        self.graph_edit.initMdl(self.tbwq.dico_wq_mod[self.cur_wq_mod])
        self.fill_tab_laws()

    def create_tab_model(self):
        """ Create table of initial concentrations"""
        self.list_trac = []
        model = QStandardItemModel()
        model.insertColumns(0, 2)
        model.setHeaderData(0, 1, 'Bief', 0)
        model.setHeaderData(1, 1, 'Abscissa', 0)

        sql = "SELECT id, sigle FROM {0}.tracer_name WHERE type = '{1}' ORDER BY id".format(self.mdb.SCHEMA,
                                                                                            self.tbwq.dico_wq_mod[
                                                                                                self.cur_wq_mod])
        rows = self.mdb.run_query(sql, fetch=True)
        model.insertColumns(2, len(rows))
        for r, row in enumerate(rows):
            model.setHeaderData(r + 2, 1, row[1], 0)
            self.list_trac.append([row[0], row[1]])

        model.itemChanged.connect(self.onTabDataChange)
        return model

    def shortCut_row_del(self):
        if self.ui.tab_laws.hasFocus():
            cols = []
            model = self.ui.tab_laws.model()
            selection = self.ui.tab_laws.selectedIndexes()
            for idx in selection:
                if idx.column() > 1:
                    model.item(idx.row(), idx.column()).setData(None, 0)
                    cols.append(idx.column() - 2)
            cols = list(set(cols))
            self.update_courbe(cols)

    def fill_tab_laws(self):
        """ fill table """
        self.ui.tab_laws.setModel(self.create_tab_model())
        if self.cur_wq_law != -1:
            self.filling_tab = True
            model = self.ui.tab_laws.model()

            if self.cur_wq_law != -1:
                sql = "SELECT distinct bief FROM {0}.init_conc_wq WHERE id_config = {1} ORDER BY bief".format(
                    self.mdb.SCHEMA,
                    self.cur_wq_law)
                lst_bief = self.mdb.run_query(sql, fetch=True)
                if len(lst_bief) > 0:
                    self.ui.cb_bief.blockSignals(True)
                    for bief in lst_bief:
                        self.ui.cb_bief.addItem("Bief {}".format(bief[0]), bief[0])
                    self.ui.cb_bief.blockSignals(False)
                    self.graph_edit.initGraph(self.cur_wq_law, lst_bief[0][0])
                else:
                    self.graph_edit.initGraph(None, None)

                c = 0
                for trac in self.list_trac:
                    sql = "SELECT bief, abscissa, value FROM {0}.init_conc_wq WHERE id_config = {1} AND id_trac = {2} " \
                          "ORDER BY  bief, abscissa".format(self.mdb.SCHEMA, self.cur_wq_law, trac[0])
                    rows = self.mdb.run_query(sql, fetch=True)
                    if c == 0:
                        model.insertRows(0, len(rows))
                        for r, row in enumerate(rows):
                            for c, val in enumerate(row):
                                if c < 2:
                                    itm = QStandardItem()
                                    itm.setData(val, 0)
                                    model.setItem(r, c, itm)
                        c = 2

                    for r, row in enumerate(rows):
                        itm = QStandardItem()
                        itm.setData(row[2], 0)
                        model.setItem(r, c, itm)

                    c += 1

            self.filling_tab = False
        else:
            self.graph_edit.initGraph(None, None)

    def import_csv(self):
        """ import CSV """
        # TODO not good format
        # +2 (bief , abscissa)
        nb_col = len(self.list_trac) + 2
        f = QFileDialog.getOpenFileName(None, 'File Selection', self.mgis.repProject, "File (*.txt *.csv)")
        if f[0] != '':
            error = False
            self.filling_tab = True
            model = self.create_tab_model()
            r = 0
            with open(f[0], "r", encoding="utf-8") as filein:
                for num_ligne, ligne in enumerate(filein):
                    if ligne[0] != '#':
                        liste = ligne.split(";")
                        if len(liste) == nb_col:
                            model.insertRow(r)
                            for c, val in enumerate(liste):
                                itm = QStandardItem()
                                if c == 0:
                                    itm.setData(data_to_int(val), 0)
                                else:
                                    itm.setData(data_to_float(val), 0)
                                model.setItem(r, c, itm)

                            r += 1
                        else:
                            error = True
                            break

            self.filling_tab = False

            if not error:
                self.ui.tab_laws.setModel(model)
                self.update_cb_bief()
                self.update_courbe("all")
            else:
                if self.mgis.DEBUG:
                    self.mgis.addInfo("Import failed ({}) because the colone number of file isn't agree.".format(f[0]))

    def current_bief(self):
        if self.ui.cb_bief.currentIndex() == -1:
            return None
        else:
            return self.ui.cb_bief.itemData(self.ui.cb_bief.currentIndex())

    def update_cb_bief(self):
        cur_bief = self.current_bief()

        lst_bief = []
        for r in range(self.ui.tab_laws.model().rowCount()):
            if self.ui.tab_laws.model().item(r, 0).data(0) not in lst_bief:
                lst_bief.append(self.ui.tab_laws.model().item(r, 0).data(0))
        lst_bief.sort()

        self.ui.cb_bief.blockSignals(True)
        self.ui.cb_bief.clear()
        for bief in lst_bief:
            self.ui.cb_bief.addItem("Bief {}".format(bief), bief)
        if cur_bief:
            self.ui.cb_bief.findData(cur_bief)
        self.ui.cb_bief.blockSignals(False)

    def change_bief(self):
        self.update_courbe("all")

    def onTabDataChange(self, itm):
        if not self.filling_tab:
            if itm.column() < 2:
                model = itm.model()
                model.sort(1)
                model.sort(0)
                idx = itm.index()
                self.ui.tab_laws.scrollTo(idx, 0)
            if itm.column() == 0:
                self.update_cb_bief()
                self.update_courbe("all")
            elif itm.column() == 1:
                self.update_courbe("all")
            elif itm.column() > 1:
                idx = itm.index()
                self.update_courbe([idx.column() - 2])

    def update_courbe(self, courbes):
        data = {}
        if courbes == "all":
            courbes = range(self.ui.tab_laws.model().columnCount() - 2)

        lx = []
        for r in range(self.ui.tab_laws.model().rowCount()):
            if self.ui.tab_laws.model().item(r, 0).data(0) == self.current_bief():
                lx.append(self.ui.tab_laws.model().item(r, 1).data(0))

        for crb in courbes:
            ly = []
            for r in range(self.ui.tab_laws.model().rowCount()):
                if self.ui.tab_laws.model().item(r, 0).data(0) == self.current_bief():
                    ly.append(self.ui.tab_laws.model().item(r, crb + 2).data(0))
            data[crb] = {"x": lx, "y": ly}

        self.graph_edit.majCourbes(data)

    def new_val(self):
        self.filling_tab = True
        model = self.ui.tab_laws.model()
        r = model.rowCount()
        model.insertRow(r)

        itm = QStandardItem()
        if r == 0:
            cur_bief = 1
        else:
            cur_bief = model.item(r - 1).data(0)
        itm.setData(cur_bief, 0)
        model.setItem(r, 0, itm)

        itm = QStandardItem()
        if r == 0:
            valabs = 0.0
        else:
            if model.item(r - 1, 0).data(0) != cur_bief:
                valabs = 0.0
            else:
                if model.item(r - 2, 0).data(0) != cur_bief:
                    valabs = model.item(r - 1, 1).data(0) + 1.
                else:
                    valabs = 2 * model.item(r - 1, 1).data(0) - model.item(r - 2, 1).data(0)
        itm.setData(valabs, 0)
        model.setItem(r, 1, itm)

        for c in range(2, model.columnCount()):
            model.setItem(r, c, QStandardItem())
        self.ui.tab_laws.scrollToBottom()
        self.filling_tab = False

        self.update_cb_bief()
        self.update_courbe("all")

    def delete_val(self):
        if self.ui.tab_laws.selectedIndexes():
            rows = [idx.row() for idx in self.ui.tab_laws.selectedIndexes()]
            rows = list(set(rows))
            rows.sort(reverse=True)
            for row in rows:
                model = self.ui.tab_laws.model()
                model.removeRow(row)
            self.update_cb_bief()
            self.update_courbe("all")

    def acceptPage2(self):
        # save Info
        # modificaito liste page 1
        # change de page
        if self.ui.tab_laws.model().rowCount() > 0:
            name_law = str(self.ui.LawWQ.text())
            if self.cur_wq_law == -1:
                if self.mgis.DEBUG:
                    self.mgis.addInfo("Addition of {} Tracer initial condition".format(name_law))
                self.mdb.execute(
                    "INSERT INTO {0}.init_conc_config (name, type) VALUES ('{1}', {2})".format(self.mdb.SCHEMA,
                                                                                               name_law,
                                                                                               self.cur_wq_mod))
                res = self.mdb.run_query("SELECT Max(id) FROM {0}.init_conc_config".format(self.mdb.SCHEMA), fetch=True)
                self.cur_wq_law = res[0][0]
            else:
                if self.mgis.DEBUG:
                    self.mgis.addInfo("Editing of {} Tracer Initial Concentration".format(name_law))
                self.mdb.execute(
                    "UPDATE {0}.init_conc_config SET name = '{1}' WHERE id = {2}".format(self.mdb.SCHEMA, name_law,
                                                                                         self.cur_wq_law))
                self.mdb.execute(
                    "DELETE FROM {0}.init_conc_wq WHERE id_config = {1}".format(self.mdb.SCHEMA, self.cur_wq_law))

            recs = []
            for r in range(self.ui.tab_laws.model().rowCount()):
                for c in range(2, self.ui.tab_laws.model().columnCount()):
                    recs.append([self.cur_wq_law, self.list_trac[c - 2][0], self.ui.tab_laws.model().item(r, 0).data(0),
                                 self.ui.tab_laws.model().item(r, 1).data(0),
                                 self.ui.tab_laws.model().item(r, c).data(0)])
            self.mdb.run_query(
                "INSERT INTO {0}.init_conc_wq (id_config, id_trac, bief, abscissa, value) VALUES (%s, %s, %s, %s, %s)".format(
                    self.mdb.SCHEMA), many=True, listMany=recs)
        else:
            self.rejectPage2()
        self.accept()

    def rejectPage2(self):
        if self.mgis.DEBUG:
            self.mgis.addInfo("Cancel of Tracer Laws")
        self.reject()


def data_to_float(txt):
    try:
        float(txt)
        return float(txt)
    except ValueError:
        return None


def data_to_int(txt):
    try:
        int(txt)
        return int(txt)
    except ValueError:
        return None


class ItemEditorFactory(
    QItemEditorFactory):  # http://doc.qt.io/qt-5/qstyleditemdelegate.html#subclassing-qstyleditemdelegate    It is possible for a custom delegate to provide editors without the use of an editor item factory. In this case, the following virtual functions must be reimplemented:
    def __init__(self):
        QItemEditorFactory.__init__(self)

    def createEditor(self, userType, parent):
        # print (userType)
        if userType == QVariant.Double or userType == 0:
            doubleSpinBox = QDoubleSpinBox(parent)
            doubleSpinBox.setDecimals(10)
            doubleSpinBox.setMinimum(-1000000000.)  # The default maximum value is 99.99.
            doubleSpinBox.setMaximum(1000000000.)  # The default maximum value is 99.99.
            return doubleSpinBox
        else:
            integerSpinBox = QSpinBox(parent)
            integerSpinBox.setMinimum(-1000000000.)  # The default maximum value is 99.99.
            integerSpinBox.setMaximum(1000000000.)  # The default maximum value is 99.99.
            return integerSpinBox
            # return ItemEditorFactory.createEditor(userType, parent)
