from PyQt5 import QtCore, QtGui, QtWidgets

class new_member(object):

    def __init__(self,Controller) -> None:
        super().__init__()
        self.Controller = Controller
    
    # def setupUi(self,Dialog):
    #     Dialog.setObjectName("Dialog")
    #     Dialog.resize(800, 800)

        # self.lineEdit = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit.setGeometry(QtCore.QRect(450, 300, 200, 41))
        # self.lineEdit.setText("")
        # self.lineEdit.setObjectName("lineEdit")

        # self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit_2.setGeometry(QtCore.QRect(450, 380, 200, 41))
        # self.lineEdit_2.setText("")
        # self.lineEdit_2.setObjectName("lineEdit_2")

        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(300, 500, 200, 100))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.go_to_menu)

        # self.label = QtWidgets.QLabel(Dialog)
        # self.label.setGeometry(QtCore.QRect(150, 300, 200, 41))

        # font = QtGui.QFont()
        # font.setPointSize(16)

        # self.label.setFont(font)
        # self.label.setObjectName("label")

        # self.label_2 = QtWidgets.QLabel(Dialog)
        # self.label_2.setGeometry(QtCore.QRect(150, 380, 200, 41))

        # font = QtGui.QFont()
        # font.setPointSize(16)

        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")

        # self.retranslateUi(Dialog)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    #     self.pushButton.setText(_translate("Dialog", "Enter"))
    #     self.label.setText(_translate("Dialog", "Customer Name :"))
    #     self.label_2.setText(_translate("Dialog", "Phone Number  :"))

    # def go_to_menu (self) :
    #     self.Controller.open_first_page()

    def setupUi(self,Dialog):
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
        Dialog.setWindowTitle(_translate("Dialog", "NEM MEMBER"))
        self.pushButton.setText(_translate("Dialog", "NEW MEMBER"))
        self.pushButton_2.setText(_translate("Dialog", "OLD MEMBER"))

    def go_to_new_member(self) :
        # print('BTN CLICK')
        self.Controller.open_first_page()
        