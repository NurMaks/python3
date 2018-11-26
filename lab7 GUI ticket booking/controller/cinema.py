from controller.database import DB

class Cinema:
    def __init__(self):
        self.id = None
        self.name = None
        self.listCinema = []
        self.getListCinema()

    def getListCinema(self):
        self.listCinema = []
        db = DB()
        data = db.select('Cinemas', ['id', 'name'])
        for item in data:
            self.listCinema.append(item)
    
    def setCinema(self, id, name):
        self.id = id
        self.name = name
        
