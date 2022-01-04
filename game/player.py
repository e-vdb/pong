import tkinter as tk


class Player:
    def __init__(self):
        self.can_play = False
        self.name = 'unknown'

    def enter_name(self):
        self.name_window = tk.Toplevel()
        lbl_enter_name = tk.Label(self.name_window, text="Enter your name", fg="black")
        lbl_enter_name.pack()
        ent_name = tk.Entry(self.name_window)
        ent_name.insert(0, 'Player')
        ent_name.pack()
        btn_enter_name = tk.Button(self.name_window, text="Enter",
                                   command=lambda: self.enter(ent_name))
        btn_enter_name.pack()

    def enter(self, name):
        self.name = name.get()
        self.name_window.destroy()
        self.can_play = True