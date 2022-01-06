
class Paddle:
    def __init__(self, can, y):
        self.can = can
        self.can.update()
        self.width = 100
        self.height = 10
        self.x = (self.can.winfo_width() - self.width) / 2
        self.y = y
        self.bar = self.can.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                             fill='white', outline='white')

    def center_bar(self):
        self.can.delete(self.bar)
        self.x = (self.can.winfo_width() - self.width) / 2
        self.bar = self.can.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                             fill='white', outline='white')

    def move_right(self, event=None,  shift=1):
        x1, _, x2, _ = self.can.coords(self.bar)
        if x2 + 10 < self.can.winfo_width():
            self.can.move(self.bar, shift, 0)

    def move_left(self, event=None, shift=-1):
        x1, _, x2, _ = self.can.coords(self.bar)
        if x1 - 10 > 0:
            self.can.move(self.bar, shift, 0)