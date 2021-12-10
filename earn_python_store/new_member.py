from PyQt5 import QtCore, QtGui, QtWidgets

class newmember(object):

    def __init__(self,Dialog) -> None:
        super().__init__()
        self.Dialog = Dialog

    def setupUi(self):
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(800, 800)

        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(450, 300, 200, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 380, 200, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 500, 200, 100))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.change_page)

        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(150, 300, 200, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 380, 200, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Customer Name :"))
        self.label_2.setText(_translate("Dialog", "Phone Number  :"))