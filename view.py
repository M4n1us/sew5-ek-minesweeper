# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from CustomButton import CustomButton

stylesheet_disabled="""
        QPushButton  {
            background-color: rgb(200, 200, 200);
            border:1px solid rgb(150, 150, 150);
        }
        """

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttons = QtWidgets.QGridLayout()
        self.buttons.setObjectName("buttons")

        self.mines = []
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.x_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.x_spin.setMinimum(2)
        self.x_spin.setMaximum(99)
        self.x_spin.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.x_spin.setProperty("value", 10)
        self.x_spin.setObjectName("x_spin")
        self.horizontalLayout_3.addWidget(self.x_spin)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.y_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.y_spin.setMinimum(2)
        self.y_spin.setProperty("value", 10)
        self.y_spin.setObjectName("y_spin")
        self.horizontalLayout_3.addWidget(self.y_spin)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.buttons.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout.addLayout(self.buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        #self.mine.setText(_translate("MainWindow", "?"))
        self.label.setText(_translate("MainWindow", "Grid width:"))
        self.label_2.setText(_translate("MainWindow", "Grid height:"))
        self.pushButton.setText(_translate("MainWindow", "Play"))

    def get_x_y(self):
        return self.x_spin.value(), self.y_spin.value()

    def teardown_menu(self):
        for i in reversed(range(self.horizontalLayout_3.count())):
            self.horizontalLayout_3.itemAt(i).widget().setParent(None)
        self.horizontalLayout_3.setParent(None)

    def disableButton(self, x, y):
        button = self.mines[y][x]
        button.setStyleSheet(stylesheet_disabled)
        button.leftclick_handler = None
        button.rightclick_handler = None

    def setupMines(self, x_count, y_count):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for y in range(y_count):
            self.mines.append([])
            for x in range(x_count):
                mine = CustomButton(self.centralwidget)
                font = mine.font()
                font.setPointSize(13)
                mine.setFont(font)
                sizePolicy.setHeightForWidth(mine.sizePolicy().hasHeightForWidth())
                mine.setSizePolicy(sizePolicy)
                mine.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
                mine.setMinimumSize(QtCore.QSize(32, 32))
                mine.setMaximumSize(QtCore.QSize(32, 32))
                mine.setFlat(False)
                mine.setObjectName("mine_%i_%i" % (x, y))

                self.mines[y].append(mine)
                self.buttons.addWidget(mine, y, x)
