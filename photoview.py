# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photoview.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import glob

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

#from pyqtgraph.Qt import QtCore, QtGui

from PyQt5.QtGui import QImage, QPixmap

import xml.etree.ElementTree as ET

import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 400, 571))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.horizontalLayout_4.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        # シグナルの設定
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.forward_photo)
        self.pushButton_2.clicked.connect(self.back_photo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.showFileDialog)
        self.tableWidget.cellClicked.connect(self.cellClick)
        self.pushButton_4.clicked.connect(self.No_Hit)
        self.pushButton_5.clicked.connect(self.Hit)
        self.action.triggered.connect(self.create_ws)
        self.pushButton_6.clicked.connect(self.save_csv)

        self.scene = GraphicsSceneForMainView()

    def forward_photo(self):
        # リストの最後まで行かなかったら次の画像へ移動
        if self.view_num < (len(self.photolist) - 1):
            self.view_num += 1
            self.graphics_view(self.photolist[self.view_num])

            # Tableの次の場所へマーク
            self.tableWidget.item(self.view_num - 1, 0).setBackground(QtGui.QColor(255, 255, 255))
            self.tableWidget.item(self.view_num, 0).setBackground(QtGui.QColor(0, 150, 150))

            # Tableの次の場所を中心に持ってくる
            self.tableWidget.scrollToItem(self.tableWidget.item(self.view_num, 0), QtWidgets.QAbstractItemView.PositionAtCenter)

    def back_photo(self):
        # リストの最初まで行かなかったら前の画像へ移動
        if self.view_num > 0:
            self.view_num -= 1
            self.graphics_view(self.photolist[self.view_num])

            # Tableの前の場所へマーク
            self.tableWidget.item(self.view_num + 1, 0).setBackground(QtGui.QColor(255, 255, 255))
            self.tableWidget.item(self.view_num, 0).setBackground(QtGui.QColor(0, 150, 150))

            # Tableの前の場所を中心に持ってくる
            self.tableWidget.scrollToItem(self.tableWidget.item(self.view_num, 0), QtWidgets.QAbstractItemView.PositionAtCenter)

    def graphics_view(self, image_path):
        # 画像の表示
        self.scene.clear_contents()
        self.org_qimg_file_path = image_path
        self.pixmap = QtGui.QImage(self.org_qimg_file_path).scaled(1000, 560)
        self.pixItem = QtGui.QPixmap.fromImage(self.pixmap)
        self.scene.addPixmap(self.pixItem)

        # sceneをgraphics_viweに追加
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "参照"))
        self.pushButton_2.setText(_translate("MainWindow", "前へ"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "A"))
        self.pushButton.setText(_translate("MainWindow", "次へ"))
        self.pushButton.setShortcut(_translate("MainWindow", "D"))
        self.groupBox.setTitle(_translate("MainWindow", "File List"))
        self.pushButton_4.setText(_translate("MainWindow", "No Hit"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "."))
        self.pushButton_5.setText(_translate("MainWindow", "Hit"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "Enter"))
        self.pushButton_6.setText(_translate("MainWindow", "保存"))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.action.setText(_translate("MainWindow", "新規作成"))
        self.action_2.setText(_translate("MainWindow", "開く"))


    def cellClick(self, row, col):
        # 前のセルの色を消す
        self.tableWidget.item(self.view_num, 0).setBackground(QtGui.QColor(255, 255, 255))

        # セルをクリックしたらその画像へジャンプする
        self.graphics_view(self.photolist[row])
        self.view_num = row

    def No_Hit(self):
        # ヒットしなかったらTableに0をセット
        item = QtWidgets.QTableWidgetItem(str(0))
        self.tableWidget.setItem(self.view_num, 1, item)

    def Hit(self):
        # ヒットしたらTableに0をセット
        item = QtWidgets.QTableWidgetItem(str(1))
        self.tableWidget.setItem(self.view_num, 1, item)

    def create_ws(self):
        # 作成するファイルの場所を開く
        self.dirname = QFileDialog.getExistingDirectory(None, "Please select photo folder")

        os.chdir(self.dirname)

        if self.dirname:
            # cfgファイルが存在するかを確認
            if not os.path.exists(self.dirname + "_cfg.xml"):
                print("create file", self.dirname + "_cfg.xml")

                # 新規 Work space(.xml)を作成
                root = ET.Element("root")
                tree = ET.ElementTree(element = root)

                folder_path = ET.SubElement(root, "folder_path")
                csv_path = ET.SubElement(root, "csv_path")

                folder_path.text = self.dirname
                print("dirname is ", self.dirname)
                csv_path.text = self.dirname + "/annotation.csv"

                tree.write(self.dirname + "_cfg.xml", encoding="utf-8", xml_declaration=True)

                # ファイルのディレクトリをtextボックスに表示
                self.dirname = self.dirname.replace("/", os.sep)
                self.lineEdit.setText(self.dirname)
                #self.btnExec.setEnabled(True)
                self.step = 0

                self.photolist = glob.glob(self.dirname + "/*.jpg")
                self.photolist.sort()
                # print("file list is ", self.photolist)

                # 最初の一枚目を表示
                self.graphics_view(self.photolist[0])
                self.view_num = 0

                # テーブルの用意
                self.colcnt = 2
                self.rowcnt = len(self.photolist)
                self.tableWidget.setColumnCount(self.colcnt)
                self.tableWidget.setRowCount(self.rowcnt)

                # annotation(.csv)の作成
                with open("annotation.csv", "w") as csv_f:
                    csv_writer = csv.writer(csv_f, lineterminator="\n")
                    for i in range(self.rowcnt):
                        item = QtWidgets.QTableWidgetItem(str(self.photolist[i][-14:]))
                        item2 = QtWidgets.QTableWidgetItem(str(""))
                        self.tableWidget.setItem(i, 0, item)
                        self.tableWidget.setItem(i, 1, item2)

                        csv_writer.writerow([self.photolist[i][-14:]])


                # Tableの最初をマーク
                self.tableWidget.item(0, 0).setBackground(QtGui.QColor(0, 150, 150))
            else:
                print("Error : cfg file(.xml) already exit")
        else:
            print("Error : Directory already exit")

    def showFileDialog(self):
        # 参照場所を開く
        self.filename = QFileDialog.getOpenFileName(None, "File open", "./", "Image files (*.xml)")[0]

        if self.filename:
            # xmlファイルの読み込み
            tree = ET.parse(self.filename)
            root = tree.getroot()

            for path in root.iter("folder_path"):
                folder_path = path.text
                self.dirname = path.text
            for path in root.iter("csv_path"):
                csv_path = path.text

            #print(self.dirname)
            os.chdir(self.dirname)

            folder_path = folder_path.replace("/", os.sep)
            self.lineEdit.setText(folder_path)
            #self.btnExec.setEnabled(True)
            self.step = 0

            self.photolist = glob.glob(folder_path + "/*.jpg")
            self.photolist.sort()
            #print("file list is ", self.photolist)

            # 最初の一枚目を表示
            self.graphics_view(self.photolist[0])
            self.view_num = 0

            # テーブルの用意
            self.colcnt = 2
            self.rowcnt = len(self.photolist)
            self.tableWidget.setColumnCount(self.colcnt)
            self.tableWidget.setRowCount(self.rowcnt)
            with open(self.dirname + csv_path, newline="") as csv_f:
                csv_reader = csv.reader(csv_f)
                csv_reader = [row for row in csv_reader]
                #print("csv is ", csv_reader)
                for i in range(self.rowcnt):
                    item = QtWidgets.QTableWidgetItem(str(self.photolist[i][-14:]))
                    item_csv = QtWidgets.QTableWidgetItem(str(csv_reader[i][1]))
                    self.tableWidget.setItem(i, 1, item_csv)
                    self.tableWidget.setItem(i, 0, item)

            # Tableの最初をマーク
            self.tableWidget.item(0, 0).setBackground(QtGui.QColor(0, 150, 150))

    def save_csv(self):
        os.chdir(self.dirname)
        with open("annotation.csv", "w") as csv_f:
            csv_writer = csv.writer(csv_f, lineterminator="\n")
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column).text()
                    row_data.append(item)
                csv_writer.writerow(row_data)
        print("saved to ", self.dirname + "/annotation.csv")

class GraphicsSceneForMainView(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None, window=None, mode="cursor"):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.parent = parent
        self.window = window
        self.mode = mode

        self.points = []
        self.line_items = []
        self.lines = []

        self.pens = []


    def set_mode(self, mode):
        self.mode = mode

    def set_img_contents(self, img_contents):
        self.set_img_contents = img_contents

    def clear_contents(self):
        self.points.clear()
        self.line_items.clear()
        self.lines.clear()
        self.pens.clear()
        self.set_img_contents = None

