from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from first_page import fist_page

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = fist_page(Dialog)
ui.setupUi()
Dialog.show()
sys.exit(app.exec_())

