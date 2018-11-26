from controller.database import DB

class MyTickets:
    def __init__(self):
        self.myTickets = []
    
    def listMyTickets(self, userId):
        self.myTickets = []
        db = DB()
        for item in db.select("Tickets", '*', 'user_id='+str(userId)):
            arr = []
            arr.append(item[2])
            arr.append(item[3])
            arr.append(item[4])
            arr.append(item[5])
            arr.append(item[6])
            arr.append(item[7])
            self.myTickets.append(arr)
        return self.myTickets
