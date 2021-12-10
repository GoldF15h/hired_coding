from PyQt5 import QtCore, QtGui, QtWidgets
import sys

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

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = first_page()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


