from DB import DB
from times import Times

class Kino:
    def __init__(self, cinemaID):
        self.kino = []
        for db in DB().select("Films", "*"):
            arr = {}
            arr["id"] = db[0]
            arr["name"] = db[1]
            self.kino.append(arr)
        self.chosenID = None
        self.cinemaID = cinemaID
        self.time = None #Times(cinemaID, self.id)
    
    def getKino(self):
        return self.kino
    
    def setChosenID(self, id):
        self.chosenID = id
        self.time = Times(self.cinemaID, self.chosenID)

    def setChosenTime(self, timeID):
        self.time.setChosenTime(timeID)

    def getTimes(self):
        return self.time.getTimes()

    def getPlaces(self):
        return self.time.getPlace()
    
    def setChosenPlaces(self, place):
        self.time.setChosenPlaces(place)