import tkinter as tk

class BuyTicket(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="Buy Ticket", font=("Helvetica", 17))
        title.pack()

        CINEMA = []
        for item in self.model.cinema.listCinema:
            CINEMA.append(item[1])
        self.variable1 = tk.StringVar(self)
        self.variable1.set(CINEMA[0])
        cinemaMenu = tk.OptionMenu(self, self.variable1, *CINEMA)
        cinemaMenu.pack(fill='x', ipady=5, pady=15)

        FILM = []
        for item in self.model.film.listFilm:
            FILM.append(item[1])
        self.variable2 = tk.StringVar(self)
        self.variable2.set(FILM[0])
        filmMenu = tk.OptionMenu(self, self.variable2, *FILM)
        filmMenu.pack(fill='x', ipady=5, pady=5)

        next = tk.Button(self, text='Next', relief=tk.GROOVE, font=("Helvetica", 12), command=self.next)
        next.pack(fill='x', pady=10, ipady=5)

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', pady=10, ipady=5)

    def next(self):
        cinema = None
        film = None
        for item in self.model.cinema.listCinema:
            if self.variable1.get() in item:
                cinema = item
                break
        for item in self.model.film.listFilm:
            if self.variable2.get() in item:
                film = item
                break
        self.model.setCinemaAndFilm(cinema, film)
        self.controller.create_pages()
        self.controller.show_page("Time")

    def back(self):
        self.controller.create_pages()
        self.controller.show_page("HomePage")