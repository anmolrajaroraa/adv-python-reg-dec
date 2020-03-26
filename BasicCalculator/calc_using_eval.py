from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(269, 0, 261, 41))
        self.label.setStyleSheet("font: 75 36pt \"Georgia\";\n"
                                 "color: rgb(32, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 100, 271, 41))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "border-color: rgb(32, 255, 255);\n"
                                    "font: 24pt \"Georgia\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 271, 31))
        self.label_2.setStyleSheet("color: rgb(32, 255, 255);\n"
                                   "font: 24pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 200, 271, 41))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(32, 255, 255);\n"
                                      "font: 24pt \"Georgia\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 210, 271, 31))
        self.label_3.setStyleSheet("color: rgb(32, 255, 255);\n"
                                   "font: 24pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 300, 271, 41))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(32, 255, 255);\n"
                                      "font: 24pt \"Georgia\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 310, 271, 31))
        self.label_4.setStyleSheet("color: rgb(32, 255, 255);\n"
                                   "font: 24pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 410, 113, 51))
        self.pushButton.setStyleSheet("background-color: rgb(32, 255, 255);\n"
                                      "font: 36pt \"Georgia\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 410, 113, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(32, 255, 255);\n"
                                        "font: 36pt \"Georgia\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 410, 113, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(32, 255, 255);\n"
                                        "font: 36pt \"Georgia\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 410, 113, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(32, 255, 255);\n"
                                        "font: 36pt \"Georgia\";")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Basic Calculator"))
        self.label_2.setText(_translate("MainWindow", "First Number"))
        self.label_3.setText(_translate("MainWindow", "Second Number"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "*"))
        self.pushButton_4.setText(_translate("MainWindow", "/"))
        self.lineEdit_3.setDisabled(True)
        self.pushButton.clicked.connect(self.calc)
        self.pushButton_2.clicked.connect(self.calc)
        self.pushButton_3.clicked.connect(self.calc)
        self.pushButton_4.clicked.connect(self.calc)

    def calc(self):
        try:
            button = self.sender()
            operator = button.text()
            first_num = self.lineEdit.text()
            second_num = self.lineEdit_2.text()
            expression = first_num + operator + second_num
            result = eval(expression)
            self.lineEdit_3.setText(str(result))
        except NameError:
            self.lineEdit_3.setText("Please enter numbers!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
