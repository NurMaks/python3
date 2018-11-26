from controller.database import DB

class Film:
    def __init__(self):
        self.id = None
        self.name = None
        self.listFilm = []
        self.getListFilm()
    
    def getListFilm(self):
        self.listFilm = []
        for db in DB().select("Films", "*"):
            arr = []
            arr.append(db[0])
            arr.append(db[1])
            self.listFilm.append(arr)
    
    def setFilm(self, id, name):
        self.id = id
        self.name = name
    