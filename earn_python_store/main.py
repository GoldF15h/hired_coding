import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from file_manage import *

cur_member_index = 0


#  ________ ___  ________  ________  _________        ________  ________  ________  _______      
# |\  _____|\  \|\   __  \|\   ____\|\___   ___\     |\   __  \|\   __  \|\   ____\|\  ___ \     
# \ \  \__/\ \  \ \  \|\  \ \  \___|\|___ \  \_|     \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|    
#  \ \   __\\ \  \ \   _  _\ \_____  \   \ \  \       \ \   ____\ \   __  \ \  \  __\ \  \_|/__  
#   \ \  \_| \ \  \ \  \\  \\|____|\  \   \ \  \       \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \ 
#    \ \__\   \ \__\ \__\\ _\ ____\_\  \   \ \__\       \ \__\    \ \__\ \__\ \_______\ \_______\
#     \|__|    \|__|\|__|\|__|\_________\   \|__|        \|__|     \|__|\|__|\|_______|\|_______|
#                            \|_________|                                                        
                                                                                               
                                                                                               
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
        self.pushButton_2.clicked.connect(self.go_to_old_member)

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

    def go_to_old_member(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = old_member()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()


#  ________   _______   ___       __           _____ ______   _______   _____ ______   ________  _______   ________     
# |\   ___  \|\  ___ \ |\  \     |\  \        |\   _ \  _   \|\  ___ \ |\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
# \ \  \\ \  \ \   __/|\ \  \    \ \  \       \ \  \\\__\ \  \ \   __/|\ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
#  \ \  \\ \  \ \  \_|/_\ \  \  __\ \  \       \ \  \\|__| \  \ \  \_|/_\ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
#   \ \  \\ \  \ \  \_|\ \ \  \|\__\_\  \       \ \  \    \ \  \ \  \_|\ \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
#    \ \__\\ \__\ \_______\ \____________\       \ \__\    \ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
#     \|__| \|__|\|_______|\|____________|        \|__|     \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                                                                                                      
                                                                                                                                                                                                         
class new_member(object):
    
    def setupUi(self, Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(450, 250, 200, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 330, 200, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 450, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_menu)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 250, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 330, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(206, 580, 380, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Customer Name :"))
        self.label_2.setText(_translate("Dialog", "Phone Number  :"))
        self.label_3.setText(_translate("Dialog", ""))

    def go_to_menu (self) :
        # print("DATA",self.lineEdit.text() , self.lineEdit_2.text())
        
        name = self.lineEdit.text()
        phone_num = self.lineEdit_2.text()

        if not(phone_num.isnumeric() and name.isalpha()) :
            self.show_err()
        else :
            member_list = read_member()
            isFound = 0
            for i in range(len(member_list)) :
                if member_list[i]['phone_num'] == phone_num :
                    member_list[i]['name'] = name
                    isFound = 1
                    break
            if isFound == 0 :
                member_list.append({'name':name,'phone_num':phone_num})
            write_member(member_list)

            self.main_dialog.hide()
            self.main_dialog = QtWidgets.QMainWindow()
            self.ui = menu()
            self.ui.setupUi(self.main_dialog,'',0)
            self.main_dialog.show()

    def show_err (self) :
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "  INPUT ERROR PLEASE REENTER"))
        self.label_3.setStyleSheet("background-color: red; border: 0px solid black;")
        QtCore.QMetaObject.connectSlotsByName(self.main_dialog)
        self.main_dialog.show()

#  ________  ___       ________          _____ ______   _______   _____ ______   ________  _______   ________     
# |\   __  \|\  \     |\   ___ \        |\   _ \  _   \|\  ___ \ |\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
# \ \  \|\  \ \  \    \ \  \_|\ \       \ \  \\\__\ \  \ \   __/|\ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
#  \ \  \\\  \ \  \    \ \  \ \\ \       \ \  \\|__| \  \ \  \_|/_\ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
#   \ \  \\\  \ \  \____\ \  \_\\ \       \ \  \    \ \  \ \  \_|\ \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
#    \ \_______\ \_______\ \_______\       \ \__\    \ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
#     \|_______|\|_______|\|_______|        \|__|     \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                                                                                                
                                                                                                                
                                                                                                                
class old_member(object):
    def setupUi(self, Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(450, 300, 200, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_member_data)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 300, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 510, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Telephone       :"))
        self.label_3.setText(_translate("Dialog", ""))

    def go_to_member_data (self) :
        
        global cur_member_index
        member_list = read_member()
        phone_num = self.lineEdit.text()
        isFound = 0

        for i in range(len(member_list)) :
            if member_list[i]['phone_num'] == phone_num :
                cur_member_index = i
                isFound = 1
                break

        if isFound == 0 :
            self.show_err()

        else :
            self.main_dialog.hide()
            self.main_dialog = QtWidgets.QMainWindow()
            self.ui = show_member_data()
            self.ui.setupUi(self.main_dialog)
            self.main_dialog.show()

    def show_err (self) :
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "    PHONE NUMBER NOT FOUND"))
        self.label_3.setStyleSheet("background-color: red; border: 0px solid black;")
        QtCore.QMetaObject.connectSlotsByName(self.main_dialog)
        self.main_dialog.show()

#  ________  ___  ___  ________  ___       __           _____ ______   _______   _____ ______   ________  _______   ________          ________  ________  _________  ________     
# |\   ____\|\  \|\  \|\   __  \|\  \     |\  \        |\   _ \  _   \|\  ___ \ |\   _ \  _   \|\   __  \|\  ___ \ |\   __  \        |\   ___ \|\   __  \|\___   ___|\   __  \    
# \ \  \___|\ \  \\\  \ \  \|\  \ \  \    \ \  \       \ \  \\\__\ \  \ \   __/|\ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \       \ \  \_|\ \ \  \|\  \|___ \  \_\ \  \|\  \   
#  \ \_____  \ \   __  \ \  \\\  \ \  \  __\ \  \       \ \  \\|__| \  \ \  \_|/_\ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\       \ \  \ \\ \ \   __  \   \ \  \ \ \   __  \  
#   \|____|\  \ \  \ \  \ \  \\\  \ \  \|\__\_\  \       \ \  \    \ \  \ \  \_|\ \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \|       \ \  \_\\ \ \  \ \  \   \ \  \ \ \  \ \  \ 
#     ____\_\  \ \__\ \__\ \_______\ \____________\       \ \__\    \ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\        \ \_______\ \__\ \__\   \ \__\ \ \__\ \__\
#    |\_________\|__|\|__|\|_______|\|____________|        \|__|     \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|        \|_______|\|__|\|__|    \|__|  \|__|\|__|
#    \|_________|                                                                                                                                                                 
                                                                                                                                                                                
                                                                                                                                                                                
class show_member_data(object):
    def setupUi(self, Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 450, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_menu)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 250, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 330, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(450, 250, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(450, 330, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        member_list = read_member()

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "Customer Name :"))
        self.label_2.setText(_translate("Dialog", "Phone Number  :"))

        global cur_member_index

        try :
            name = member_list[cur_member_index]['name']
            phone_number = member_list[cur_member_index]['phone_num']
        except :
            name = ''
            phone_number = ''

        self.label_4.setText(_translate("Dialog", name))
        self.label_5.setText(_translate("Dialog", phone_number))

    def go_to_menu (self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog,'',0)
        self.main_dialog.show()

#  ________  ___  ___  ________  ________  ________  _______           _____ ______   _______   ________   ___  ___     
# |\   ____\|\  \|\  \|\   __  \|\   __  \|\   ____\|\  ___ \         |\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    
# \ \  \___|\ \  \\\  \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   
#  \ \  \    \ \   __  \ \  \\\  \ \  \\\  \ \_____  \ \  \_|/__       \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  
#   \ \  \____\ \  \ \  \ \  \\\  \ \  \\\  \|____|\  \ \  \_|\ \       \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ 
#    \ \_______\ \__\ \__\ \_______\ \_______\____\_\  \ \_______\       \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\
#     \|_______|\|__|\|__|\|_______|\|_______|\_________\|_______|        \|__|     \|__|\|_______|\|__| \|__|\|_______|
#                                            \|_________|                                                               
                                                                                                                      
                                                                                                                      
                                                  
class choose_menu(object):
    def setupUi(self, Dialog):
        self.main_dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 200, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_to_dessert)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 250, 200, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.go_to_coffee)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 400, 200, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.go_to_tea)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 400, 200, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.go_to_juice)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Dessert"))
        self.pushButton_2.setText(_translate("Dialog", "Coffee"))
        self.pushButton_3.setText(_translate("Dialog", "Tea"))
        self.pushButton_4.setText(_translate("Dialog", "Juice"))

    def go_to_dessert(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()

    def go_to_coffee(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()

    def go_to_tea(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()

    def go_to_juice(self) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog)
        self.main_dialog.show()
                                                  
#  _____ ______   _______   ________   ___  ___     
# |\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    
# \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   
#  \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  
#   \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ 
#    \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\
#     \|__|     \|__|\|_______|\|__| \|__|\|_______|
                                                  
                                                  
                                                  
class menu(object):
    def setupUi(self, Dialog,file,page):
        # print(file,page)
        self.main_dialog = Dialog
        self.file = file
        self.page = page

        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 750, 130, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.go_to_Dessert)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 750, 130, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.go_to_Coffee)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 750, 130, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.go_to_Tea)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 750, 130, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.go_to_Juice)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 750, 130, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.go_to_Recipt)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(680, 720, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.go_right)
        self.pushButton.setText('>')
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 720, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.go_left)
        self.pushButton_2.setText('<')

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        if file == 'Dessert.txt' :
            self.pushButton_3.setFont(font)
        if file == 'Coffee.txt' :
            self.pushButton_4.setFont(font)
        if file == 'Tea.txt' :
            self.pushButton_5.setFont(font)
        if file == 'Juice.txt' :
            self.pushButton_6.setFont(font)

        self.menu_list = read_menu(file)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.max_page = (len(self.menu_list) + 19) // 20 

        cur_page = str(page+1)
        self.label.setText( cur_page + '/' + str( self.max_page ) )

        self.menu_list = self.menu_list[page*20 : page*20 + 20:]
            

        self.show_menu_list = []
        
        left_space = 80
        top_space = 30
        menu_top_space = top_space + 60
        for i in range(len(self.menu_list)) :
            # print(self.menu_list[i])
            shifter = 30 * i
            self.checkBox = QtWidgets.QCheckBox(Dialog)
            self.checkBox.setGeometry(QtCore.QRect(left_space , menu_top_space + shifter, 21, 17))
            self.checkBox.setText("")

            # self.checkBox.setObjectName("checkBox")
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(left_space + 60, menu_top_space + shifter, 141, 16))
            self.label.setText(self.menu_list[i][0])

            self.lineEdit = QtWidgets.QLineEdit(Dialog)
            self.lineEdit.setGeometry(QtCore.QRect(left_space + 280, menu_top_space + shifter, 113, 20))

            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(left_space + 570, menu_top_space + shifter, 141, 16))
            self.label_2.setText(self.menu_list[i][1])

        # self.checkBox = QtWidgets.QCheckBox(Dialog)
        # self.checkBox.setGeometry(QtCore.QRect(50, 100, 21, 17))
        # self.checkBox.setText("")
        # # self.checkBox.setObjectName("checkBox")
        # self.label = QtWidgets.QLabel(Dialog)
        # self.label.setGeometry(QtCore.QRect(110, 100, 141, 16))
        # self.label.setText('ShowName')
        # self.lineEdit = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit.setGeometry(QtCore.QRect(330, 100, 113, 20))
        # self.label_2 = QtWidgets.QLabel(Dialog)
        # self.label_2.setGeometry(QtCore.QRect(620, 100, 141, 16))
        # self.label_2.setText('ShowPrice')

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(left_space, top_space, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(left_space+60, top_space, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(left_space+310, top_space, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(left_space+570, top_space, 141, 16))
        self.label_6.setObjectName("label_6")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Dessert"))
        self.pushButton_4.setText(_translate("Dialog", "Coffee"))
        self.pushButton_5.setText(_translate("Dialog", "Tea"))
        self.pushButton_6.setText(_translate("Dialog", "Juice"))
        self.pushButton_7.setText(_translate("Dialog", "Recipt"))
        self.label_3.setText(_translate("Dialog", "Select"))
        self.label_4.setText(_translate("Dialog", "Name"))
        self.label_5.setText(_translate("Dialog", "Amount"))
        self.label_6.setText(_translate("Dialog", "Price"))
        # self.pushButton.setText(_translate("Dialog", ">"))
        # self.pushButton_2.setText(_translate("Dialog", "<"))

    def go_to_Dessert(self) :
        self.update_menu('Dessert.txt',0)
    
    def go_to_Coffee(self) :
        self.update_menu('Coffee.txt',0)

    def go_to_Tea(self) :
        self.update_menu('Tea.txt',0)

    def go_to_Juice(self) :
        self.update_menu('Juice.txt',0)

    def go_to_Recipt(self) :
        pass

    def go_right(self) :
        if self.page < self.max_page - 1 :
            self.update_menu(self.file,self.page+1)

    def go_left(self) :
        if self.page > 0 :
            self.update_menu(self.file,self.page-1)

    def update_menu(self,file,page) :
        self.main_dialog.hide()
        self.main_dialog = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.main_dialog,file,page)
        self.main_dialog.show()


#  _____ ______   ________  ___  ________      
# |\   _ \  _   \|\   __  \|\  \|\   ___  \    
# \ \  \\\__\ \  \ \  \|\  \ \  \ \  \\ \  \   
#  \ \  \\|__| \  \ \   __  \ \  \ \  \\ \  \  
#   \ \  \    \ \  \ \  \ \  \ \  \ \  \\ \  \ 
#    \ \__\    \ \__\ \__\ \__\ \__\ \__\\ \__\
#     \|__|     \|__|\|__|\|__|\|__|\|__| \|__|
                                             
                                             
                                             
if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    Dialog = QtWidgets.QMainWindow()
    # ui = first_page()
    ui = menu()
    ui.setupUi(Dialog,'Dessert.txt',0)
    Dialog.show()
    sys.exit(app.exec_())



