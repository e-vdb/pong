import tkinter as tk
from help_functions import about, printRules
from ball import Ball
from bar import Bar
from player import Player
import time

Refresh_Sec = 0.005
Ball_min_movement = 1
colors = ['red', 'green', 'yellow', 'blue']


class Game(tk.Frame):
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.player = Player()
        self.player_IA = Player()
        self.make_widgets()
        self.bar = Bar(self.can, 550)
        self.bar_IA = Bar(self.can, 40)
        self.bar_IA.center_bar()
        self.ball = Ball(self.can, self.bar, self.bar_IA, self.player, self.player_IA)


    def make_widgets(self):
        self.label = tk.Label(self, text="Click on Game to start a new game", fg="black", font='Helvetica 14')
        self.label.pack(side=tk.TOP)
        self.countdown = tk.StringVar()
        self.lbl_countdown = tk.Label(self, textvariable=self.countdown,  fg="black", font='Helvetica 20')
        self.countdown.set("")
        self.lbl_countdown.pack(side=tk.TOP)
        self.can = tk.Canvas(self, bg='black', height=600, width=500)
        self.can.pack(side=tk.TOP, padx=5, pady=5)
        self.score = tk.StringVar()
        self.score.set(self.player.score)
        self.score_IA = tk.StringVar()
        self.score_IA.set(self.player_IA.score)
        tk.Label(self, text='Human = ', fg="red", font='Helvetica 20').pack(side=tk.LEFT)
        self.lbl_score = tk.Label(self, textvariable=self.score, fg="red", font='Helvetica 20')
        self.lbl_score_IA = tk.Label(self, textvariable=self.score_IA, fg="red", font='Helvetica 20')
        self.lbl_score.pack(side=tk.LEFT)
        self.lbl_score_IA.pack(side=tk.RIGHT)
        tk.Label(self, text='Computer = ', fg="red", font='Helvetica 20').pack(side=tk.RIGHT)


    def play(self):
        self.bar.center_bar()
        self.bar_IA.center_bar()
        if self.player.can_play:
            self.label.configure(text='Keep the ball in motion!!!')
            self.ball.ball_in_motion = True
            if self.ball.ball_in_motion:
                self.ball.play()
            self.update_scores()
            if self.player.score == 5:
                self.game_over()
            elif self.player_IA.score == 5:
                self.game_over()
            else:
                self.new_game()

    def new_game(self):
        try:
            self.can.delete(self.ball.ball)
        except:
            pass
        self.bar.center_bar()
        self.player.can_play = True
        self.label.configure(text='Get ready')
        value_countdown = 5
        self.countdown.set(str(value_countdown))
        for i in range(5):
            self.update()
            value_countdown -= 1
            self.countdown.set(str(value_countdown))
            time.sleep(1)
        self.countdown.set('')
        self.play()

    def reset_game(self):
        self.player.reset()
        self.player_IA.reset()
        self.update_scores()
        self.new_game()

    def update_scores(self):
        self.score.set(self.player.score)
        self.score_IA.set(self.player_IA.score)
        self.update()

    def game_over(self):
        self.label.configure(text='Game over.')
        self.player.can_play = False


window = tk.Tk()
window.title("Moving ball")
frame = tk.Frame(window)
frame.pack(side=tk.TOP)

game = Game(window)
game.pack(side=tk.TOP)
#Menus
top = tk.Menu(window)
window.config(menu=top)

game_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=game_menu)
game_menu.add_command(label='New game', command=game.reset_game)
game_menu.add_command(label='Exit', command=window.destroy)

help_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='How to play?', command=printRules)
help_menu.add_command(label='About', command=about)

window.bind("<Left>", lambda event,x=-10: game.bar.move_left(event,x))
window.bind("<Right>", lambda event,x=10: game.bar.move_right(event,x))

window.mainloop()
