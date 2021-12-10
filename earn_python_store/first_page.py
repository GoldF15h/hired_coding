import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from new_member import newmember

class fist_page(object):

    def __init__(self,Dialog) -> None:
        super().__init__()
        self.Dialog = Dialog

    def setupUi(self):
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(800, 800)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 391, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change_page)

        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 410, 391, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.change_page)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "NEW MEMBER"))
        self.pushButton_2.setText(_translate("Dialog", "OLD MEMBER"))

    def change_page(self) :
        self.Dialog.close()
        self.Dialog = QtWidgets.QDialog()
        ui = newmember(self.Dialog)
        ui.setupUi()
        self.Dialog.show()