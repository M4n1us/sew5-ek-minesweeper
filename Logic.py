import random


class GameLogic():
    def __init__(self, controller):
        self.field_values = []
        self.covered_tiles = []
        self.mine_char = "X"
        self.mine_percentage = 5
        self.controller = controller

    def generate_mines(self, x, y):
        for y_pos in range(y):
            self.field_values.append([])
            for x_pos in range(x):
                rand = random.randint(1, 100)
                if rand <= self.mine_percentage:
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

    def restart_game(self):
        self.field_values = []
        self.covered_tiles = []

    def leftclick_button(self, button, x, y):
        if self.field_values[y][x] == self.mine_char:
            self.controller.end_game(button)
        elif int(self.field_values[y][x]) == 0:
            self.flood_fill(x, y)
            self.check_has_won()
        else:
            self.controller.myForm.disableButton(x, y)
            self.controller.myForm.mines[y][x].setText(str(self.field_values[y][x]))
            self.check_has_won()

    def check_has_won(self):
        if self.has_won():
            self.controller.has_won()



    def has_won(self):
        ret = True

        x, y = self.controller.myForm.get_x_y()
        for y_pos in range(y):
            for x_pos in range(x):
                is_not_mine = self.field_values[y_pos][x_pos] != self.mine_char
                is_not_flag = self.field_values[y_pos][x_pos] != "?" and self.field_values[y_pos][x_pos] != "!"
                has_not_been_revealed = self.controller.myForm.mines[y_pos][x_pos].text() != str(self.field_values[y_pos][x_pos])
                if is_not_mine and is_not_flag and has_not_been_revealed:
                    ret = False
                    break
            if not ret:
                break
        return ret

    def flood_fill(self, x_start, y_start):
        x_size, y_size = len(self.field_values[0]), len(self.field_values)
        stack = {(x_start, y_start)}

        crater = []

        while stack:
            point = stack.pop()
            x, y = point
            not_handled = point not in crater
            not_covered = point not in self.covered_tiles
            valid = self.element_has_no_mines(x, y)
            if not_handled and not_covered and valid:

                crater.append(point)
                self.covered_tiles.append(point)
                if x > 0 and self.element_has_no_mines(x - 1, y):
                    stack.add((x - 1, y))
                if x < (x_size - 1) and self.element_has_no_mines(x + 1, y):
                    stack.add((x + 1, y))
                if y > 0 and self.element_has_no_mines(x, y - 1):
                    stack.add((x, y - 1))
                if y < (y_size - 1) and self.element_has_no_mines(x, y + 1):
                    stack.add((x, y + 1))

        edges = set()

        for x, y in crater:
            edges.add((x,y+1))
            edges.add((x-1,y+1))
            edges.add((x-1,y))
            edges.add((x-1,y-1))
            edges.add((x,y-1))
            edges.add((x+1,y-1))
            edges.add((x+1,y))
            edges.add((x+1,y+1))

        for x, y in crater:
            self.controller.myForm.disableButton(x, y)
            self.controller.myForm.mines[y][x].setText(str(self.field_values[y][x]))

        for x, y in edges:
            if (x, y) not in crater and 0 <= x < x_size and 0 <= y < y_size:
                self.controller.myForm.disableButton(x, y)
                self.controller.myForm.mines[y][x].setText(str(self.field_values[y][x]))

    def element_has_no_mines(self, x, y):
        return int(self.field_values[y][x]) == 0

    def rightclick_button(self, button, x, y):
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

    def get_button_text(self, x, y):
        return str(self.field_values[y][x])