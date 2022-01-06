import random
import time

Refresh_Sec = 0.005
Ball_min_movement = 1
colors = ['red', 'green', 'yellow', 'blue']
shifts = [1, 1.25, 1.5, 1.75]
ball_shift = {col: shift for col, shift in zip(colors, shifts)}

class Ball:
    def __init__(self, can, bar, bar_IA, player, player_IA, refresh_Sec=Refresh_Sec):
        self.can = can
        self.refresh_Sec = refresh_Sec
        self.radius = 25
        self.x = self.can.winfo_width()/2
        self.y = self.can.winfo_height()/2
        self.shift = shifts[0]
        self.shift_x = self.shift * random.choice((-1, 1))
        self.shift_y = self.shift * random.choice((-1, 1))
        self.ball_in_motion = False
        self.color = colors[0]
        self.bar = bar
        self.bar_IA = bar_IA
        self.player = player
        self.player_IA = player_IA

    def reset(self):
        self.x = self.can.winfo_width()/2
        self.y = self.can.winfo_height()/2
        self.color = colors[0]
        self.shift = ball_shift[self.color]
        self.shift_x = self.shift * random.choice((-1, 1))
        self.shift_y = self.shift * random.choice((-1, 1))
        self.ball = self.can.create_oval(self.x, self.y, self.x + self.radius, self.y + self.radius,
                                         fill=self.color, outline='white')

    def change_color(self):
        self.color = random.choice(colors)
        self.can.itemconfig(self.ball, fill=self.color)
        self.shift = ball_shift[self.color]
        self.shift_x = self.shift if self.shift_x > 0 else -self.shift
        self.shift_y = self.shift if self.shift_y > 0 else -self.shift

    def motion(self):
        self.can.move(self.ball, self.shift_x, self.shift_y)
        self.can.update()
        time.sleep(self.refresh_Sec)
        ball_pos = self.can.coords(self.ball)
        bar_x1, bar_y1, bar_x2, bar_y2 = self.can.coords(self.bar.bar)
        bar_IA_x1, bar_IA_y1, bar_IA_x2, bar_IA_y2 = self.can.coords(self.bar_IA.bar)
        x1, y1, x2, y2 = ball_pos
        if x1 < 0 or x2 > self.can.winfo_width():
            self.change_color()
            self.shift_x = - self.shift_x
        if abs(y2 - bar_y2) < self.shift:
            if (bar_x1 <= x1 <= bar_x2) or (bar_x1 <= x2 <= bar_x2):
                self.shift_y = - self.shift_y
        elif abs(y1 - bar_IA_y1) < self.shift:
            if (bar_IA_x1 <= x1 <= bar_IA_x2) or (bar_IA_x1 <= x2 <= bar_IA_x2):
                self.shift_y = - self.shift_y
        elif y1 < 0:
            self.stop()
            self.player.score += 1
        elif y2 > self.can.winfo_height():
            self.stop()
            self.player_IA.score += 1

    def moving_bar_IA(self):
        try:
            x1, y1, x2, y2 = self.can.coords(self.ball)
            bar_IA_x1, bar_IA_y1, bar_IA_x2, bar_IA_y2 = self.can.coords(self.bar_IA.bar)
            if bar_IA_x1 < x1 < bar_IA_x2:
                self.can.update()
            if x1 > bar_IA_x2:
                self.bar_IA.move_right()
                self.can.update()
            else:
                self.bar_IA.move_left()
                self.can.update()
        except:
            pass

    def play(self):
        self.reset()
        self.ball_in_motion = True
        while self.ball_in_motion:
            self.motion()
            self.moving_bar_IA()

    def stop(self):
        self.ball_in_motion = False
        self.can.delete(self.ball)