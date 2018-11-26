import tkinter as tk

class Time(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="Buy Ticket", font=("Helvetica", 17))
        title.pack()

        listTime = tk.Listbox(self)
        listTime.pack(fill='x')
        for index, item in zip(range(1, len(self.model.time.listTime)+1),self.model.time.listTime):
            listTime.insert('end', str(index)+".  time: "+item['time']+" | price: "+str(item['price'])+'\n')
        
        self.errorLabel = tk.Label(self, text="", font=("Helvetica", 10), fg='red')
        self.errorLabel.pack(fill='x')

        self.entryTime = tk.Entry(self)
        self.entryTime.pack(fill='x', ipady=5)

        next = tk.Button(self, text='Next', relief=tk.GROOVE, font=("Helvetica", 12), command=self.next)
        next.pack(fill='x', pady=15, ipady=5)

        back = tk.Button(self, text='Back', relief=tk.GROOVE, font=("Helvetica", 12), command=self.back)
        back.pack(fill='x', ipady=5)
    
    def next(self):
        timeID = self.entryTime.get()
        try:
            timeID = int(timeID)-1
        except:
            self.errorLabel.config(text="Please, enter INTEGER numbers!")
            return
        self.errorLabel.config(text="")
        if timeID < 0 or timeID > len(self.model.time.listTime)-1:
            self.errorLabel.config(text="Select a time that does not exceed the ID time")
            return
        self.model.setTime(self.model.time.listTime[timeID])
        self.controller.create_pages()
        self.controller.show_page("Place")        
        

    def back(self):
        self.controller.create_pages()
        self.controller.show_page("BuyTicket")