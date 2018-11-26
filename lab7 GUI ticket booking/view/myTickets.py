import tkinter as tk

class MyTickets(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="MY TICKETS", font=("Helvetica", 20))
        title.pack()

        listTickets = tk.Listbox(self)
        listTickets.pack(fill='x')
        for item in self.model.myTickets.myTickets:
            listTickets.insert('end', "Cinema: "+str(item[0])+"\n")
            listTickets.insert('end', "Film:   "+str(item[1])+"\n")
            listTickets.insert('end', "Time:   "+str(item[2])+"\n")
            listTickets.insert('end', "Places: "+str(item[3])+"\n")
            listTickets.insert('end', "Price:  "+str(item[4])+"\n")
            listTickets.insert('end', "Total Price: "+str(item[5])+"\n")
            listTickets.insert('end', "---------------------------------------------------------\n")

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', pady=10, ipady=5)
    
    def back(self):
        self.controller.create_pages()
        self.controller.show_page("HomePage")
