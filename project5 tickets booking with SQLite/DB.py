import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('tickets.db')
        self.c = self.conn.cursor()
    
    def close(self):
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def select(self, table, getData, where=None):
        data = []
        select = ""
        for get in getData:
            select += get + ", "
        select = select[:-2]
        if where == None:
            data = self.c.execute("SELECT "+select+" FROM "+table)
        else:
            data = self.c.execute("SELECT "+select+" FROM "+table+" WHERE "+where)
        return data.fetchall()

    def change(self, table, setData, where):
        self.c.execute("UPDATE "+table+" SET "+setData+" WHERE "+where)
        self.conn.commit()

    def insertUser(self, id, login, password, name):
        request = "INSERT INTO User (user_id, login, password, name) VALUES ("+str(id)+", '"+str(login)+"', '"+str(password)+"', '"+str(name)+"');"
        self.c.execute(request)
        self.conn.commit()
    
    def insertTicket(self, user_id, cinema, kino, time, place, price, totalPrice):
        ticket = self.select("Tickets", "*")
        id = ticket[len(ticket)-1][0]+1
        request = "INSERT INTO Tickets VALUES ("+str(id)+", "+str(user_id)+", '"+cinema+"', '"+kino+"', '"+time+"', '"+str(place)[1:-1]+"', "+str(price)+", "+str(totalPrice)+");"
        self.c.execute(request)
        self.conn.commit()

# Tables:
# Cinema => cinema_id, cinema
# Kino   => kino_id, kino
# Time   => time_id, cinema_id, kino_id, time, price
# Hall   => hall_id, time_id, placeNumber, status
# User   => user_id INTEGER, login TEXT, password TEXT, name TEXT
# Tickets => ticket_id INTEGER, user_id INTEGER, cinema TEXT, kino TEXT, time TEXT, place TEXT, price REAL, totalPrice REAL