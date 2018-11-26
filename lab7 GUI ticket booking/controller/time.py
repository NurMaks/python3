from controller.database import DB

class Time:
    def __init__(self):
        self.id = None
        self.time = None
        self.price = None
        self.listTime = []

    def getListTime(self, cinemaID, filmID):
        self.listTime = []
        db = DB()
        for db in DB().select("Times", "*", "cinema_id="+str(cinemaID)+" AND film_id="+str(filmID)):
            arr = {}
            arr["id"] = db[0]
            arr['time'] = db[3]
            arr['price'] = db[4]
            self.listTime.append(arr)
    
    def setTime(self, time):
        self.id = time['id']
        self.time = time['time']
        self.price = time['price']