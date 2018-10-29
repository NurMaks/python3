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


# Tables:
# Cinema => cinema_id, cinema
# Kino   => kino_id, kino
# Time   => time_id, cinema_id, kino_id, time, price
# Hall   => hall_id, time_id, placeNumber, status