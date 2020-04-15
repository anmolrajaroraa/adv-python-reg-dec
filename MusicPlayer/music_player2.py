# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music_player.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
import pygame
import random
import mutagen
import threading
import time
pygame.mixer.init()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.path = "/Users/anmolrajarora/Documents/adv-python-reg-dec/MusicPlayer/"
        self.isShuffle = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 159, 371, 401))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(15, 31, 261, 361))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(285, 31, 71, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 0, 251, 31))
        self.label.setStyleSheet("font: 75 24pt \"Rosewood Std\";\n"
                                 "background-color: transparent;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(420, 160, 371, 401))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 351, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 80)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 251, 31))
        self.label_2.setStyleSheet("font: 75 24pt \"Rosewood Std\";\n"
                                   "background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 71, 71))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            f"background-image : url({self.path + 'assets/shuffle_btn.png'}); background-color : white;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(95, 80, 71, 71))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            f"background-image : url({self.path + 'assets/prev_btn.png'}); background-color : white;")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 80, 71, 71))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            f"background-image : url({self.path + 'assets/next_btn.png'}); background-color : white;")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(245, 80, 71, 71))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            f"background-image : url({self.path + 'assets/play_btn.png'}); background-color : white;")
        self.pushButton_4.setIcon(QtGui.QIcon(
            self.path + 'assets/play_btn.png'))
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(370, 110, 371, 51))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 130, 60, 16))
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 791, 61))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 20, 113, 21))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 641, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(325, 75, 461, 50))
        self.label_7.setStyleSheet(
            "font: 75 24pt \"Cochin\"; background-color : transparent; color : rgb(0,0,0)")
        self.label_7.setObjectName("label_7")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(-1, -1, 811, 601))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 810, 703))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        image = QtGui.QPixmap(self.path + "assets/bg.jpg")
        self.label_5.setPixmap(image)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(335, 461, 140, 41))
        self.pushButton_6.setStyleSheet(
            "font: 75 24pt \"Cochin\"; background-color : yellow; color : black")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(210, 60, 461, 50))
        self.label_6.setStyleSheet(
            "font: 75 36pt \"Cochin\"; background-color : transparent; color : rgb(255,255,255)")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Playlist = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist.setObjectName("actionSave_Playlist")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave_Playlist_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist_2.setObjectName("actionSave_Playlist_2")
        self.actionQuit_3 = QtWidgets.QAction(MainWindow)
        self.actionQuit_3.setObjectName("actionQuit_3")
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionSave_Playlist_2)
        self.menuFile.addAction(self.actionQuit_3)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Featured Songs"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Very Long Song Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actions"))
        self.label_2.setText(_translate("MainWindow", "Playlist"))
        self.label_3.setText(_translate("MainWindow", "00:00"))
        self.label_4.setText(_translate("MainWindow", "00:00"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.lineEdit.setPlaceholderText("Search a song...")
        self.pushButton_6.setText(_translate("MainWindow", "Continue >>>"))
        self.label_6.setText(_translate(
            "MainWindow", "Welcome to Xomp Player"))
        self.label_7.setText(_translate(
            "MainWindow", "Currently playing : "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_Playlist.setText(
            _translate("MainWindow", "Save Playlist"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionSave_Playlist_2.setText(
            _translate("MainWindow", "Save Playlist"))
        self.actionQuit_3.setText(_translate("MainWindow", "Quit"))
        self.pushButton_6.clicked.connect(self.frame_4.hide)
        self.pushButton.clicked.connect(self.toggleShuffle)
        self.pushButton_2.clicked.connect(self.previousSong)
        self.pushButton_3.clicked.connect(self.nextSong)
        self.songs = os.listdir(
            "/Users/anmolrajarora/Documents/adv-python-reg-dec/MusicPlayer/songs")
        # print(self.songs)
        for i in range(len(self.songs)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.item(i).setText(self.songs[i])
            self.listWidget.setStyleSheet(
                "font: 75 15pt \"Cochin\";\n")
            item = QtWidgets.QListWidgetItem()
            self.listWidget_2.addItem(item)
            self.listWidget_2.item(i).setIcon(
                QtGui.QIcon(f"{self.path}assets/play_btn.png"))

        item = QtWidgets.QTableWidgetItem()
        item.setText("Raat Di Gedi - Diljit Dosanjh (DjPunjab.Com).mp3")
        item2 = QtWidgets.QTableWidgetItem()
        item2.setText("delete btn")
        self.rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowCount)
        self.tableWidget.setItem(self.rowCount, 0, item)
        self.tableWidget.setItem(self.rowCount, 1, item2)

        self.listWidget.itemClicked.connect(self.selectSong)
        self.listWidget_2.itemClicked.connect(self.addToPlaylist)
        self.tableWidget.itemClicked.connect(self.printItem)
        self.pushButton_4.clicked.connect(self.playSong)

        self.horizontalSlider.sliderPressed.connect(self.changeValue)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setDisabled(True)
        self.t = threading.Thread(target=self.changeSliderPosition)
        self.t.start()

    def printItem(self, item):
        print(item)
        print(item.text())

    def addToPlaylist(self, item):
        for i in range(self.listWidget_2.count()):
            if item == self.listWidget_2.item(i):
                print(i)

    def selectSong(self, item):
        self.selectedSong = item.text()
        print(self.selectedSong)

    def playSong(self):
        pygame.mixer.music.load(self.path + "songs/" + self.selectedSong)
        pygame.mixer.music.play()
        self.label_7.setText("Currently playing : " + self.selectedSong)
        self.horizontalSlider.setDisabled(False)
        songFile = mutagen.File(self.path + "songs/" + self.selectedSong)
        songLength = songFile.info.length
        self.horizontalSlider.setMaximum(songLength)
        print("Song played..")

    def nextSong(self):
        if self.isShuffle:
            index = random.randint(0, len(self.songs) - 1)
        else:
            index = self.songs.index(self.selectedSong)
            index += 1
            if index == len(self.songs):
                index = 0
        self.selectedSong = self.songs[index]
        print(self.selectedSong)
        self.playSong()

    def previousSong(self):
        if self.isShuffle:
            index = random.randint(0, len(self.songs) - 1)
        else:
            index = self.songs.index(self.selectedSong)
            index -= 1
            if index == -1:
                index = len(self.songs) - 1
        self.selectedSong = self.songs[index]
        print(self.selectedSong)
        self.playSong()

    def toggleShuffle(self):
        self.isShuffle = not self.isShuffle
        if self.isShuffle:
            self.pushButton.setStyleSheet(
                f"background-image : url({self.path + 'assets/shuffle_btn.png'}); background-color : blue;")
            self.nextSong()
        else:
            self.pushButton.setStyleSheet(
                f"background-image : url({self.path + 'assets/shuffle_btn.png'}); background-color : white;")

    def changeValue(self):
        print("Position changed")
        currentValue = self.horizontalSlider.value()
        print(currentValue)
        pygame.mixer.music.set_pos(currentValue)

    def changeSliderPosition(self):
        while True:
            print("Slider Position changed")
            songPos = pygame.mixer.music.get_pos()
            print(songPos/1000)
            seconds = songPos / 1000
            time.sleep(1)
            self.horizontalSlider.setValue(seconds)
            self.label_3.setText(f"00:{int(seconds)}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
