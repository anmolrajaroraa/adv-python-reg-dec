from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 822)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 200, 481, 531))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(35, 70, 301, 421))
        self.listWidget.setObjectName("listWidget")
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(370, 70, 81, 421))
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(144, -10, 191, 81))
        self.label_3.setStyleSheet("font: 24pt \"Gabriola\";\n"
                                   "color: rgb(85, 170, 255);\n"
                                   "background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(550, 200, 461, 531))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(180, -10, 151, 81))
        self.label_4.setStyleSheet("font: 24pt \"Gabriola\";\n"
                                   "background-color: transparent;\n"
                                   "color: rgb(0, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 381, 411))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 110, 981, 80))
        self.frame_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 31, 41))
        # self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);
        self.pushButton.setStyleSheet("background-color : white;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.setIcon(QtGui.QIcon('E:\\desktopApp\\assets\\playbtn.png'))

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 20, 31, 41))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 20, 31, 41))
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 20, 31, 41))
        self.pushButton_4.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(340, 30, 541, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(294, 30, 31, 21))
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(910, 30, 31, 21))
        self.label_2.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 20, 981, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 771, 41))
        self.lineEdit.setStyleSheet("color: rgb(170, 0, 0);\n"
                                    "background-color: rgb(0, 0, 0);\n"
                                    "font: 8pt \"Cambria Math\";\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 20, 41, 41))
        self.pushButton_5.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(-1, -1, 1051, 741))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(-10, 10, 1141, 810))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        image = QtGui.QPixmap("E:\\desktopApp\\bg.jpg")
        self.label_5.setPixmap(image)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 600, 121, 71))
        self.pushButton_6.setStyleSheet("font: 75 10pt \"Georgia\";\n"
                                        "background-color: transparent;\n"
                                        "color: rgb(85, 170, 255);\n")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(260, 110, 451, 101))
        self.label_6.setStyleSheet("font: 75 24pt \"Nirmala UI\";\n"
                                   "color: rgb(0, 85, 255);\n"
                                   "background-color: transparent;\n"
                                   "")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCreate_new_playlist = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_playlist.setObjectName(
            "actionCreate_new_playlist")
        self.actionSave_Playlist = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist.setObjectName("actionSave_Playlist")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCreate_new_playlist)
        self.menuFile.addAction(self.actionSave_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Featured Songs"))
        self.label_4.setText(_translate("MainWindow", "PlayList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Song Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actions"))
        self.label.setText(_translate("MainWindow", "0:00"))
        self.label_2.setText(_translate("MainWindow", "0:00"))
        self.lineEdit.setText(_translate(
            "MainWindow", "Search songs here...!!!"))
        self.pushButton_6.setText(_translate("MainWindow", "Continue -->>"))
        self.label_6.setText(_translate(
            "MainWindow", "Welcome to Xomp Player"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCreate_new_playlist.setText(
            _translate("MainWindow", "Create new playlist"))
        self.actionSave_Playlist.setText(
            _translate("MainWindow", "Save Playlist"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.pushButton_6.clicked.connect(self.frame_5.hide)

        # os.chdir('E:\\desktopApp\\songs')
        songs = os.listdir()
        for i in range(len(songs)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.item(i).setText(songs[i])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
