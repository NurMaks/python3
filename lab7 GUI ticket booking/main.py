import tkinter as tk
from view.welcome import Welcome
from view.login import Login
from view.signin import Signin
from view.homePage import HomePage
from controller.model import Model
from view.myTickets import MyTickets

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ticket Booking System")
        self.geometry("650x450+350+100")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(side='top', expand=True)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.pages = {}
        self.create_pages()
    
    def create_pages(self):
        model = Model()
        arr = [
            'Welcome',
            'Login',
            'Signin',
            'HomePage',
            'MyTickets'
        ]
        for page in arr:
            frame = eval(page)(self.container, self, model)
            frame.grid(row=0, column=0, sticky='wsne', ipadx=100, ipady=10)
            self.pages[page] = frame
        
        self.show_page("Welcome")
    
    def show_page(self, page):
        frame = self.pages[page]
        frame.tkraise()

if __name__ == "__main__":
    app = Main()
    app.mainloop()