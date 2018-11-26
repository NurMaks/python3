from controller.user import User
from controller.myTickets import MyTickets
from controller.cinema import Cinema
from controller.film import Film
from controller.time import Time
from controller.place import Place
from controller.database import DB

class Model:
    def __init__(self):
        self.user = User()
        self.myTickets = MyTickets()
        self.cinema = Cinema()
        self.film = Film()
        self.time = Time()
        self.place = Place()
        self.db = DB()
        
    def setCinemaAndFilm(self, cinema, film):
        self.cinema.setCinema(cinema[0], cinema[1])
        self.film.setFilm(film[0], film[1])
        self.time.getListTime(cinema[0], film[0])
    
    def setTime(self, time):
        self.time.setTime(time)
        self.place.getListPlaces(time['id'])
    
    def saveTicket(self, place):
        self.place.setPlace(place)
        totalPrice = self.time.price * len(self.place.place)
        self.db.insertTicket(self.user.id, self.cinema.name, self.film.name, self.time.time, self.place.place, self.time.price, totalPrice)