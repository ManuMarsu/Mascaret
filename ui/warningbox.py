

from qgis.PyQt.QtCore import qVersion
if int(qVersion()[0])<5:
    from qgis.PyQt.QtWidgets import QMessageBox
else:     #qt5
    from qgis.PyQt.QtGui import QMessageBox


class Class_warningBox():
    """TODO add all select box """
    def __init__(self, mgis):
        self.mgis = mgis
        self.mdb = self.mgis.mdb

    def yes_no_q(self, msg, title=''):
        d = QMessageBox()
        d.setWindowTitle(title)
        d.addButton(QMessageBox.Yes)
        d.addButton(QMessageBox.No)
        d.setDefaultButton(QMessageBox.No)
        d.setText(msg)
        ret =d.exec_()

        if ret == QMessageBox.Yes:
            return True
        else:
            return False