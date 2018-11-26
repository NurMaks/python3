from controller.database import DB

class Place:
    def __init__(self):
        self.place = []
        self.listPlace = []
    
    def getListPlaces(self, timeID):
        self.listPlace = []
        for db in DB().select("Halls", "*", "time_id="+str(timeID)):
            arr = {}
            arr["id"] = db[0]
            arr['place'] = db[2]
            arr['status'] = db[3]
            self.listPlace.append(arr)
        
    def setPlace(self, place):
        self.place = place
        for item in self.listPlace:
            if item['place'] in place:
                DB().change("Halls", "status=1", "id="+str(item['id']))