from PyQt5 import QtCore, QtGui, QtWidgets
from first_page import first_page

class new_member(object):
    
    def setupUi(self,Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(450, 300, 200, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 380, 200, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 500, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_menu)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 300, 200, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 380, 200, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Customer Name :"))
        self.label_2.setText(_translate("Dialog", "Phone Number  :"))

    def go_to_menu (self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = first_page()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()

        