# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popuperror.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        ERR_Dialog.setObjectName("Dialog")
        ERR_Dialog.resize(400, 122)
        self.label = QtWidgets.QLabel(ERR_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(ERR_Dialog)
        _translate = QtCore.QCoreApplication.translate
        ERR_Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "INPUT ERROR PLEASE REENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
