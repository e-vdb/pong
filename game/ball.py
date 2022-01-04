import random
import time

Refresh_Sec = 0.005
Ball_min_movement = 1
colors = ['red', 'green', 'yellow', 'blue']


class Ball:
    def __init__(self, can, bar, bar_IA, player, player_IA, refresh_Sec=Refresh_Sec):
        self.can = can
        self.refresh_Sec = refresh_Sec
        self.radius = 25
        self.x = self.can.winfo_width()/2
        self.y = self.can.winfo_height()/2
        self.shift_x = Ball_min_movement
        self.shift_y = Ball_min_movement * random.choice((-1, 1))
        self.ball_in_motion = False
        self.color = colors[0]
        self.bar = bar
        self.bar_IA = bar_IA
        self.player = player
        self.player_IA = player_IA

    def reset(self):
        self.x = self.can.winfo_width()/2
        self.y = self.can.winfo_height()/2
        self.shift_y = Ball_min_movement * random.choice((-1, 1))
        self.ball = self.can.create_oval(self.x, self.y, self.x + self.radius, self.y + self.radius,
                                         fill='red', outline='white')

    def change_color(self):
        index_color = colors.index(self.color)
        if index_color < len(colors) - 1:
            self.color = colors[index_color + 1]
        else:
            self.color = colors[0]
        self.can.itemconfig(self.ball, fill=self.color)

    def motion(self):
        self.can.move(self.ball, self.shift_x, self.shift_y)
        self.can.update()
        time.sleep(self.refresh_Sec)
        ball_pos = self.can.coords(self.ball)
        bar_x1, bar_y1, bar_x2, bar_y2 = self.can.coords(self.bar.bar)
        bar_IA_x1, bar_IA_y1, bar_IA_x2, bar_IA_y2 = self.can.coords(self.bar_IA.bar)
        x1, y1, x2, y2 = ball_pos
        if x1 < 0 or x2 > self.can.winfo_width():
            self.shift_x = - self.shift_x
            self.change_color()
        if y2 == bar_y2:
            if (bar_x1 <= x1 <= bar_x2) or (bar_x1 <= x2 <= bar_x2):
                self.shift_y = - self.shift_y
        elif y1 == bar_IA_y1:
            if (bar_IA_x1 <= x1 <= bar_IA_x2) or (bar_IA_x1 <= x2 <= bar_IA_x2):
                self.shift_y = - self.shift_y
        elif y1 < 0:
            self.stop()
            self.player.score += 1
        elif y2 > self.can.winfo_height():
            self.stop()
            self.player_IA.score += 1

    def moving_bar_IA(self):
        if self.shift_x > 0:
            self.bar_IA.move_right()
            self.can.update()
        else:
            self.bar_IA.move_left()
            self.can.update()

    def play(self):
        self.reset()
        self.ball_in_motion = True
        while self.ball_in_motion:
            self.motion()
            self.moving_bar_IA()

    def stop(self):
        self.ball_in_motion = False
        self.can.delete(self.ball)