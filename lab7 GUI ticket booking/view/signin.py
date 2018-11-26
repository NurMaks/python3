import tkinter as tk

class Signin(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="S I G N I N", font=("Helvetica", 20))
        title.pack()

        form = tk.Frame(self)
        form.pack(fill="x", pady=15)

        labelLogin = tk.Label(form, text='Login:', font=("Helvetica", 12))
        labelLogin.grid(row=0, column=0, ipady=5, pady=5, sticky='w')

        labelPassword = tk.Label(form, text='Password:', font=("Helvetica", 12))
        labelPassword.grid(row=1, column=0, ipady=5, pady=5, sticky='w')

        labelName = tk.Label(form, text='Name:', font=("Helvetica", 12))
        labelName.grid(row=2, column=0, ipady=5, pady=5, sticky='w')

        labelSurname = tk.Label(form, text='Surname:', font=("Helvetica", 12))
        labelSurname.grid(row=3, column=0, ipady=5, pady=5, sticky='w')

        self.entryLogin = tk.Entry(form)
        self.entryLogin.grid(row=0, column=1, ipady=5, pady=5)

        self.entryPassword = tk.Entry(form)
        self.entryPassword.grid(row=1, column=1, ipady=5, pady=5)

        self.entryName = tk.Entry(form)
        self.entryName.grid(row=2, column=1, ipady=5, pady=5)

        self.entrySurname = tk.Entry(form)
        self.entrySurname.grid(row=3, column=1, ipady=5, pady=5)

        self.errorLabel = tk.Label(self, text="", font=("Helvetica", 10), fg='red')
        self.errorLabel.pack(fill='x')

        buttonSignin = tk.Button(self, text='Signin', relief=tk.GROOVE, font=("Helvetica", 12), command=self.button_signin)
        buttonSignin.pack(fill='x', pady=10, ipady=5)

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', pady=10, ipady=5)
    
    def button_signin(self):
        login = self.entryLogin.get()
        password = self.entryPassword.get()
        name = self.entryName.get()
        surname = self.entrySurname.get()
        if login and password and name and surname:
            if self.model.user.createUser(login, password, name, surname):
                self.controller.show_page("HomePage")
            else:
                self.errorLabel.config(text='Choose another login. This already exists')
        else:
            self.errorLabel.config(text='E R R O R')
        
    def back(self):
        self.controller.create_pages()
        self.controller.show_page("Welcome")