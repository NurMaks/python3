import tkinter as tk

class Welcome(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.model = model
        
        frame = tk.Frame(self)
        frame.pack(side='top', fill='both')

        title = tk.Label(self, text="W E L C O M E", font=("Helvetica", 20))
        title.pack()

        login = tk.Button(self, text='Log In', relief=tk.GROOVE, font=("Helvetica", 12), command=lambda:controller.show_page("Login"))
        login.pack(fill='x', pady=20, ipady=10)

        signin = tk.Button(self, text='Sign In', relief=tk.GROOVE, font=("Helvetica", 12), command=lambda:controller.show_page("Signin"))
        signin.pack(fill='x', ipady=10)
    