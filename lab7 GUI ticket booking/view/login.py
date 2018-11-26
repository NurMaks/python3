import tkinter as tk
from controller.model import Model

class Login(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="L O G I N", font=("Helvetica", 20))
        title.pack()

        form = tk.Frame(self)
        form.pack(fill="x", pady=15)

        labelLogin = tk.Label(form, text='Login:', font=("Helvetica", 12))
        labelLogin.grid(row=0, column=0, ipady=5, pady=5, sticky='w')

        labelPassword = tk.Label(form, text='Password:', font=("Helvetica", 12))
        labelPassword.grid(row=1, column=0, ipady=5, pady=5, sticky='w')

        self.entryLogin = tk.Entry(form)
        self.entryLogin.grid(row=0, column=1, ipady=5, pady=5)

        self.entryPassword = tk.Entry(form)
        self.entryPassword.grid(row=1, column=1, ipady=5, pady=5)

        self.errorLabel = tk.Label(self, text="", font=("Helvetica", 10), fg='red')
        self.errorLabel.pack(fill='x')

        buttonLogin = tk.Button(self, text='Login', relief=tk.GROOVE, font=("Helvetica", 12), command=self.button_login)
        buttonLogin.pack(fill='x', pady=10, ipady=5)

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', pady=10, ipady=5)
    
    def button_login(self):
        login = self.entryLogin.get()
        password = self.entryPassword.get()
        if self.model.user.checkUser(login, password):
            self.entryLogin.config(text="")
            self.entryPassword.config(text='')
            self.controller.create_pages()
            self.controller.show_page("HomePage")
        else:
            self.errorLabel.config(text="Wrong login or password. Try again")
    
    def back(self):
        self.controller.create_pages()
        self.controller.show_page("Welcome")