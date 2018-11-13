import psycopg2

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(database="Movie List", user="postgres", password="maksat", host="localhost", port="5432")
        self.c = self.conn.cursor()
    
    def close(self):
        self.conn.commit()
        self.c.close()
        self.conn.close()

    def select(self, table, getData, where=None):
        select = ""
        for get in getData:
            select += get + ", "
        select = select[:-2]
        if where == None:
            self.c.execute("SELECT "+select+" FROM "+table)
        else:
            self.c.execute("SELECT "+select+" FROM "+table+" WHERE "+where)
        return self.c.fetchall()

    def change(self, table, setData, where):
        self.c.execute("UPDATE "+table+" SET "+setData+" WHERE "+where)
        self.conn.commit()

    def insertUser(self, id, login, password, name, surname):
        request = "INSERT INTO Users VALUES ("+str(id)+", '"+str(login)+"', '"+str(password)+"', '"+str(name)+"', '"+str(surname)+"');"
        self.c.execute(request)
        self.conn.commit()
    
    def insertTicket(self, user_id, cinema, kino, time, place, price, totalPrice):
        ticket = self.select("Tickets", "*")
        id = 0
        if ticket:
            id = ticket[len(ticket)-1][0]+1
        else:
            id = 1
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