from DB import DB

class Place:
    def __init__(self, timeID):
        self.place = []
        for db in DB().select("Halls", "*", "time_id="+str(timeID)):
            arr = {}
            arr["id"] = db[0]
            arr['place'] = db[2]
            arr['status'] = db[3]
            self.place.append(arr)
    
    def getPlaces(self):
        return self.place

    def setChosenPlaces(self, place):
        self.chosenPlaces = place
        db = DB()
        for pl in self.chosenPlaces:
            id = self.place[0]['id']+pl-1
            db.change("Halls", "status=1", "id="+str(id))