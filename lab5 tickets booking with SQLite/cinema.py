from kino import Kino

class Cinema:
    def __init__(self, id, name):
        self.id = id
        self.kino = Kino(self.id)
        self.name = name
        self.listKino = self.kino.getKino()
        self.chosenID = None

    def setChosenKino(self, id):
        self.chosenID = id
        self.kino.setChosenID(self.chosenID)

    def getTimes(self):
        return self.kino.getTimes()

    def __str__(self):
        return "{} {}".format(self.id, self.name)
    
    def setChosenTime(self, timeID):
        self.kino.setChosenTime(timeID)

    def getPlaces(self):
        return self.kino.getPlaces()
    
    def setChosenPlaces(self, place):
        self.kino.setChosenPlaces(place)