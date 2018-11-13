from ticket import Ticket
from DB import DB

class User:
    def __init__(self):
        self.id = None
        self.login = None
        self.password = None
        self.name = None
        self.db = DB()
        self.tickets = []
    
    def checkUser(self, login, password):
        user = None
        try:
            user = self.db.select("Users", "*", "login='"+str(login)+"';")
        except:
            return False
        if user:
            if user[0][1]==login and user[0][2]==password:
                self.id = int(user[0][0])
                self.name = user[0][3]
                self.surname = user[0][4]
                self.login = user[0][1]
                self.password = user[0][2]
                return True
        return False

    
    def createUser(self, login, password, name, surname):
        user = None
        try:
            user = self.db.select("Users", "*", "login='"+str(login)+"';")
        except:
            pass
        if user:
            return False
        user = self.db.select("Users", "*")
        if user:
            self.id = int(user[len(user)-1][0])+1
        else:
            self.id = 1
        self.name = name
        self.login = login
        self.password = password
        self.surname = surname
        self.db.insertUser(self.id, login, password, name, surname)
        return True
    
    def setTicket(self, ticket):
        self.tickets.append(ticket)
        self.db.insertTicket(self.id, ticket.cinemaName, ticket.kino, ticket.time, ticket.place, ticket.price, ticket.totalPrice)
    
    def myTickets(self):
        arr = []
        db = DB()
        for item in db.select("Tickets", '*', 'user_id='+str(self.id)):
            ticket = Ticket()
            ticket.cinemaName = item[2]
            ticket.kino = item[3]
            ticket.time = item[4]
            ticket.place = item[5]
            ticket.price = item[6]
            ticket.totalPrice = item[7]
            arr.append(ticket)
        return arr
        