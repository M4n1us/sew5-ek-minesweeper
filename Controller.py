import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from view import Ui_MainWindow


class Controller(QMainWindow):
    """
        Controller for the program, adding events to the ui
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.myForm = Ui_MainWindow()
        self.myForm.setupUi(self)
        self.myForm.pushButton.clicked.connect(self.start_game)
        self.field_values = []
        self.mine_char = "X"

    def start_game(self):
        x, y = self.myForm.get_x_y()
        self.myForm.teardown_menu()
        self.myForm.setupMines(x, y)
        for row in self.myForm.mines:
            for item in row:
                item.leftclick_handler = self.click_button
                item.rightclick_handler = self.right_button
        self.generate_mines(x, y)
        self.generate_mine_numbers(x, y)
        for y_pos in range(y):
            for x_pos in range(x):
                self.myForm.mines[y_pos][x_pos].setText(str(self.field_values[y_pos][x_pos]))

    def generate_mines(self, x, y):
        for y_pos in range(y):
            self.field_values.append([])
            for x_pos in range(x):
                rand = random.randint(1, 100)
                if rand <= 20:
                    self.field_values[y_pos].append(self.mine_char)
                else:
                    self.field_values[y_pos].append(0)

    def generate_mine_numbers(self, x, y):
        for y_pos in range(y):
            for x_pos in range(x):
                if self.field_values[y_pos][x_pos] == self.mine_char:
                    if y_pos == 0:
                        if x_pos == 0:
                            self.handle_top_left(x_pos, y_pos)
                        elif x_pos == x-1:
                            self.handle_top_right(x_pos, y_pos)
                        else:
                            self.handle_top_row(x_pos, y_pos)
                    elif y_pos == y-1:
                        if x_pos == 0:
                            self.handle_bottom_left(x_pos, y_pos)
                        elif x_pos == x-1:
                            self.handle_bottom_right(x_pos, y_pos)
                        else:
                            self.handle_bottom_row(x_pos, y_pos)
                    elif y_pos != 0 and y_pos != y-1:
                        if x_pos == 0:
                            self.handle_left_row(x_pos, y_pos)
                        elif x_pos == x-1:
                            self.handle_right_row(x_pos, y_pos)
                        else:
                            self.handle_core(x_pos, y_pos)

    def handle_core(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos+1] != self.mine_char:
            self.field_values[y_pos][x_pos+1] += 1
        if self.field_values[y_pos+1][x_pos+1] != self.mine_char:
            self.field_values[y_pos+1][x_pos+1] += 1
        if self.field_values[y_pos+1][x_pos] != self.mine_char:
            self.field_values[y_pos+1][x_pos] += 1
        if self.field_values[y_pos+1][x_pos-1] != self.mine_char:
            self.field_values[y_pos+1][x_pos-1] += 1
        if self.field_values[y_pos][x_pos-1] != self.mine_char:
            self.field_values[y_pos][x_pos-1] += 1
        if self.field_values[y_pos-1][x_pos-1] != self.mine_char:
            self.field_values[y_pos-1][x_pos-1] += 1
        if self.field_values[y_pos-1][x_pos] != self.mine_char:
            self.field_values[y_pos-1][x_pos] += 1
        if self.field_values[y_pos-1][x_pos+1] != self.mine_char:
            self.field_values[y_pos-1][x_pos+1] += 1

    def handle_bottom_row(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos-1] != self.mine_char:
            self.field_values[y_pos][x_pos-1] += 1
        if self.field_values[y_pos -1][x_pos-1] != self.mine_char:
            self.field_values[y_pos -1][x_pos-1] += 1
        if self.field_values[y_pos-1][x_pos] != self.mine_char:
            self.field_values[y_pos-1][x_pos] += 1
        if self.field_values[y_pos-1][x_pos+1] != self.mine_char:
            self.field_values[y_pos-1][x_pos+1] += 1
        if self.field_values[y_pos][x_pos+1] != self.mine_char:
            self.field_values[y_pos][x_pos+1] += 1

    def handle_top_row(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos-1] != self.mine_char:
            self.field_values[y_pos][x_pos-1] += 1
        if self.field_values[y_pos +1][x_pos-1] != self.mine_char:
            self.field_values[y_pos +1][x_pos-1] += 1
        if self.field_values[y_pos+1][x_pos] != self.mine_char:
            self.field_values[y_pos+1][x_pos] += 1
        if self.field_values[y_pos+1][x_pos+1] != self.mine_char:
            self.field_values[y_pos+1][x_pos+1] += 1
        if self.field_values[y_pos][x_pos+1] != self.mine_char:
            self.field_values[y_pos][x_pos+1] += 1

    def handle_right_row(self, x_pos, y_pos):
        if self.field_values[y_pos -1][x_pos] != self.mine_char:
            self.field_values[y_pos -1][x_pos] += 1
        if self.field_values[y_pos -1][x_pos-1] != self.mine_char:
            self.field_values[y_pos -1][x_pos-1] += 1
        if self.field_values[y_pos][x_pos-1] != self.mine_char:
            self.field_values[y_pos][x_pos-1] += 1
        if self.field_values[y_pos+1][x_pos-1] != self.mine_char:
            self.field_values[y_pos+1][x_pos-1] += 1
        if self.field_values[y_pos+1][x_pos] != self.mine_char:
            self.field_values[y_pos+1][x_pos] += 1

    def handle_left_row(self, x_pos, y_pos):
        if self.field_values[y_pos -1][x_pos] != self.mine_char:
            self.field_values[y_pos -1][x_pos] += 1
        if self.field_values[y_pos -1][x_pos+1] != self.mine_char:
            self.field_values[y_pos -1][x_pos+1] += 1
        if self.field_values[y_pos][x_pos+1] != self.mine_char:
            self.field_values[y_pos][x_pos+1] += 1
        if self.field_values[y_pos+1][x_pos+1] != self.mine_char:
            self.field_values[y_pos+1][x_pos+1] += 1
        if self.field_values[y_pos+1][x_pos] != self.mine_char:
            self.field_values[y_pos+1][x_pos] += 1

    def handle_bottom_left(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos + 1] != self.mine_char:
            self.field_values[y_pos][x_pos + 1] += 1
        if self.field_values[y_pos - 1][x_pos] != self.mine_char:
            self.field_values[y_pos - 1][x_pos] += 1
        if self.field_values[y_pos - 1][x_pos + 1] != self.mine_char:
            self.field_values[y_pos - 1][x_pos + 1] += 1

    def handle_bottom_right(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos - 1] != self.mine_char:
            self.field_values[y_pos][x_pos - 1] += 1
        if self.field_values[y_pos - 1][x_pos] != self.mine_char:
            self.field_values[y_pos - 1][x_pos] += 1
        if self.field_values[y_pos - 1][x_pos - 1] != self.mine_char:
            self.field_values[y_pos - 1][x_pos - 1] += 1

    def handle_top_right(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos - 1] != self.mine_char:
            self.field_values[y_pos][x_pos - 1] += 1
        if self.field_values[y_pos + 1][x_pos] != self.mine_char:
            self.field_values[y_pos + 1][x_pos] += 1
        if self.field_values[y_pos + 1][x_pos - 1] != self.mine_char:
            self.field_values[y_pos + 1][x_pos - 1] += 1

    def handle_top_left(self, x_pos, y_pos):
        if self.field_values[y_pos][x_pos + 1] != self.mine_char:
            self.field_values[y_pos][x_pos + 1] += 1
        if self.field_values[y_pos + 1][x_pos] != self.mine_char:
            self.field_values[y_pos + 1][x_pos] += 1
        if self.field_values[y_pos + 1][x_pos + 1] != self.mine_char:
            self.field_values[y_pos + 1][x_pos + 1] += 1


    def click_button(self, button, x, y):
        #self.myForm.disableButton(x, y)
        pass

    def right_button(self, button, x, y):
        current_text = button.text()
        next_text = self.cycle_text(current_text)
        button.setText(next_text)

    def cycle_text(self, current):
        if current == "":
            return "?"
        elif current == "?":
            return "!"
        elif current == "!":
            return ""
        else:
            return current


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())