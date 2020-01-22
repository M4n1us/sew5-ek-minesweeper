import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from Logic import GameLogic
from view import Ui_MainWindow


class Controller(QMainWindow):
    """
        Controller for the program, adding events to the ui
    """
    def __init__(self, parent=None):
        """
        Initializes Controller and connects the logic with the UI
        :param parent: Parent window for UI
        """
        super().__init__(parent)

        self.myForm = Ui_MainWindow()
        self.myForm.setupUi(self)
        self.myForm.pushButton.clicked.connect(self.start_game)
        self.myForm.b1.clicked.connect(self.restart_game)

        self.logic = GameLogic(self)

    def start_game(self):
        """
        Initializes the game window content and generates mines on the logic component
        :return: none
        """
        x, y = self.myForm.get_x_y()
        self.myForm.teardown_menu()
        self.myForm.setupMines(x, y)
        for row in self.myForm.mines:
            for item in row:
                item.leftclick_handler = self.logic.leftclick_button
                item.rightclick_handler = self.logic.rightclick_button
        self.logic.generate_mines(x, y)
        self.logic.generate_mine_numbers(x, y)

    def restart_game(self):
        """
        Restarts the game by tearing down the UI, show restart game window and resets the logic
        :return: none
        """
        self.myForm.teardown_game()
        self.myForm.showStart()
        self.logic.restart_game()
        self.myForm.pushButton.clicked.connect(self.start_game)
        self.myForm.d.close()

    def has_won(self):
        """
        Handles the has_won event, when triggered locks all fields and shows win window
        :return: none
        """
        x, y = self.myForm.get_x_y()
        for y_pos in range(y):
            for x_pos in range(x):
                self.set_button_text(x_pos, y_pos)
                self.myForm.disableButton(x_pos, y_pos)
        self.myForm.showWinRestart()

    def end_game(self, button):
        """
        Triggered when a mine is hit. Locks all fields and sets mine to red
        :param button: button from which the event is triggered
        :return: none
        """
        x, y = self.myForm.get_x_y()
        for y_pos in range(y):
            for x_pos in range(x):
                self.set_button_text(x_pos, y_pos)
                self.myForm.disableButton(x_pos, y_pos)
        button.setStyleSheet("""
        QPushButton { background-color: red }
        """)
        self.myForm.showRestart()

    def set_button_text(self, x, y):
        """
        Merges data from logic component into the UI component on coordinate
        :param x: coordinate
        :param y: coordinate
        :return: none
        """
        self.myForm.mines[y][x].setText(str(self.logic.get_field_text(x, y)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())