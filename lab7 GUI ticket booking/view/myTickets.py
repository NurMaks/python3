import tkinter as tk

class MyTickets(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="MY TICKETS", font=("Helvetica", 20))
        title.pack()
