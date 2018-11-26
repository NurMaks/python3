import tkinter as tk

class Place(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model
        self.freePlaces = []

        title = tk.Label(self, text="Buy Ticket", font=("Helvetica", 20))
        title.pack()

        listPlace = tk.Listbox(self)
        listPlace.pack(fill='x')
        for item in self.model.place.listPlace:
            if item['status'] != 1:
                self.freePlaces.append(item['place'])
                listPlace.insert('end', str(item['place'])+'\n')

        self.errorLabel = tk.Label(self, text="", font=("Helvetica", 10), fg='red')
        self.errorLabel.pack(fill='x')

        self.entryPlace = tk.Entry(self)
        self.entryPlace.pack(fill='x', ipady=5)

        next = tk.Button(self, text='B U Y', relief=tk.GROOVE, font=("Helvetica", 12), command=self.next)
        next.pack(fill='x', pady=15, ipady=5)

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', pady=10, ipady=5)
    
    def next(self):
        place = self.entryPlace.get()
        if not place:
            self.errorLabel.config(text="Please, choose the place!")
            return
        try:
            place = [int(item) for item in place.split()]
        except:
            self.errorLabel.config(text="Please, enter INTEGER numbers!")
            return
        ch = True
        for item in place:
            if not item in self.freePlaces:
                ch = False
                break
        if not ch:
            self.errorLabel.config(text="Please select only free places!")
            return
        self.model.saveTicket(place)
        self.model.myTickets.listMyTickets(self.model.user.id)
        self.controller.create_pages()
        self.controller.show_page("MyTickets")
        

    def back(self):
        self.controller.create_pages()
        self.controller.show_page("Time")