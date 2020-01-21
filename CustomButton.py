from PyQt5.QtWidgets import QPushButton


class CustomButton(QPushButton):
    def __init__(self, arg, leftclick_handler=None, rightclick_handler=None):
        super().__init__(arg)
        self.leftclick = 1
        self.rightclick = 2
        self.leftclick_handler = leftclick_handler
        self.rightclick_handler = rightclick_handler

    def mousePressEvent(self, event):
        name = self.objectName().split("_")
        if event.button() == self.leftclick:
            if self.leftclick_handler is not None:
                self.leftclick_handler(self, int(name[1]), int(name[2]))
        elif event.button() == self.rightclick:
            if self.rightclick_handler is not None:
                self.rightclick_handler(self, int(name[1]), int(name[2]))
