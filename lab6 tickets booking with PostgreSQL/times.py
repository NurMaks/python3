from DB import DB
from place import Place

class Times:
    def __init__(self, cinemaID, kinoID):
        self.time = []
        for db in DB().select("Times", "*", "cinema_id="+str(cinemaID)+" AND film_id="+str(kinoID)):
            arr = {}
            arr["id"] = db[0]
            arr['time'] = db[3]
            arr['price'] = db[4]
            self.time.append(arr)
        self.chosenID = None
    
    def getTimes(self):
        return self.time
        
    def setChosenTime(self, id):
        self.chosenID = id
        self.place = Place(self.chosenID)

    def getPlace(self):
        return self.place.getPlaces()
    
    def setChosenPlaces(self, place):
        self.place.setChosenPlaces(place)