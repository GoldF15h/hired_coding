from PyQt5 import QtCore, QtGui, QtWidgets
from new_member import new_member


class first_page(object):

    def setupUi(self,Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 391, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_new_member)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 410, 391, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.go_to_new_member)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FIRST PAGE"))
        self.pushButton.setText(_translate("Dialog", "NEW MEMBER"))
        self.pushButton_2.setText(_translate("Dialog", "OLD MEMBER"))

    def go_to_new_member(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = new_member()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()