from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from first_page import fist_page
from new_member import new_member

class Controller () :
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
    def open_first_page (self) :
        self.Dialog.close()
        self.Dialog = QtWidgets.QDialog()
        ui = fist_page(self)
        ui.setupUi(self.Dialog)
        self.Dialog.show()
        # sys.exit(self.app.exec_())

    def open_new_member (self) : 
        self.Dialog.close()
        self.Dialog = QtWidgets.QDialog()
        ui = new_member(self)
        ui.setupUi(self.Dialog)
        self.Dialog.show()
        sys.exit(self.app.exec_())

app = Controller()
# app.open_first_page()
app.open_new_member()
