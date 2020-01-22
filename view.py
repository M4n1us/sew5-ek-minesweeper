from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton

from CustomButton import CustomButton

stylesheet_disabled="""
        QPushButton  {
            background-color: rgb(200, 200, 200);
            border:1px solid rgb(150, 150, 150);
        }
        """

class Ui_MainWindow(object):
    """
    UI Component based on PyQt5 for a minesweeper game, base elements are generated via QtDesigner
    """
    def setupUi(self, MainWindow):
        """
        Sets up initial UI
        :param MainWindow: Parent window
        :return: none
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttons = QtWidgets.QGridLayout()
        self.buttons.setObjectName("buttons")

        self.mines = []
        self.showStart()

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

        self.d = QDialog()
        self.b1 = QPushButton("Restart", self.d)
        self.b1.move(50, 50)
        self.d.setWindowModality(QtCore.Qt.ApplicationModal)

    def showStart(self):
        """
        Shows start UI to input game field data and launch the game
        :return: none
        """
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

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Grid width:"))
        self.label_2.setText(_translate("MainWindow", "Grid height:"))
        self.pushButton.setText(_translate("MainWindow", "Play"))

    def retranslateUi(self, MainWindow):
        """
        Translates UI Elements to system language
        :param MainWindow: Parent window
        :return: none
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper"))
        self.label.setText(_translate("MainWindow", "Grid width:"))
        self.label_2.setText(_translate("MainWindow", "Grid height:"))
        self.pushButton.setText(_translate("MainWindow", "Play"))

    def showRestart(self):
        """
        Shows Restart Game UI
        :return: None
        """
        self.d.setWindowTitle("Restart?")
        self.d.exec_()

    def showWinRestart(self):
        """
        Shows Game Won UI
        :return:
        """
        self.d.setWindowTitle("You Won")
        self.d.exec_()

    def get_x_y(self):
        """
        Gets x/y size from UI
        :return: Tuple (x,y)
        """
        return self.x_spin.value(), self.y_spin.value()

    def teardown_game(self):
        """
        Removes all game elements from the UI
        :return:
        """
        for i in reversed(range(self.buttons.count())):
            self.buttons.itemAt(i).widget().setParent(None)
        self.mines = []

    def teardown_menu(self):
        """
        Removes all Menui Elements from the UI
        :return: none
        """
        for i in reversed(range(self.horizontalLayout_3.count())):
            self.horizontalLayout_3.itemAt(i).widget().setParent(None)
        self.horizontalLayout_3.setParent(None)

    def disableButton(self, x, y):
        """
        Disables button to be non clickable and changes style to display button status
        :param x: int for the x Pos
        :param y: int for the y Pos
        :return: none
        """
        button = self.mines[y][x]
        button.setStyleSheet(stylesheet_disabled)
        button.leftclick_handler = None
        button.rightclick_handler = None

    def setupMines(self, x_count, y_count):
        """
        Generates playable mine fields in UI
        :param x_count: mine columns to generate
        :param y_count: mine rows to generate
        :return: none
        """
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
