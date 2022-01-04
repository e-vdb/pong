import tkinter as tk
from help_functions import about, printRules
from ball import Ball
from bar import Bar
from player import Player

Refresh_Sec = 0.005
Ball_min_movement = 1
colors = ['red', 'green', 'yellow', 'blue']


class Game(tk.Frame):
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.make_widgets()
        self.bar = Bar(self.can, 550)
        self.bar_IA = Bar(self.can, 40)
        self.bar_IA.center_bar()
        self.ball = Ball(self.can, self.bar, self.bar_IA)
        self.player = Player()

    def make_widgets(self):
        self.can = tk.Canvas(self, bg='black', height=600, width=500)
        self.can.pack(side=tk.TOP, padx=5, pady=5)
        self.label = tk.Label(self, text="Click on Game to start a new game", fg="black", font='Helvetica 14')
        self.label.pack(side=tk.TOP)

    def play(self):
        self.bar.center_bar()
        self.bar_IA.center_bar()
        if self.player.can_play:
            self.label.configure(text='Keep the ball in motion!!!')
            self.ball.ball_in_motion = True
            if self.ball.ball_in_motion:
                self.ball.play()
            self.game_over()

    def new_game(self):
        self.bar.center_bar()
        self.player.enter_name()
        self.label.configure(text='Click on play to start the game.')
        self.after(5000, self.play)

    def game_over(self):
        self.label.configure(text='Game over. Click on play to try again.')


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
game_menu.add_command(label='New game', command=game.new_game)
game_menu.add_command(label='Exit', command=window.destroy)

help_menu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='How to play?', command=printRules)
help_menu.add_command(label='About', command=about)

btn = tk.Button(frame, text='Play', command=game.play)
btn.pack()

window.bind("<Left>", lambda event,x=-10: game.bar.move_left(event,x))
window.bind("<Right>", lambda event,x=10: game.bar.move_right(event,x))

window.mainloop()