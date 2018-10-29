
class Ticket:
    def __init__(self, cinema):
        self.cinemaName = cinema.name
        self.kino = cinema.kino.getKino()[cinema.kino.chosenID]['name']
        for x in cinema.getTimes():
            if x['id'] == cinema.kino.time.chosenID:
                self.time = x['time']
                self.price = x['price']
                break
        self.place = cinema.kino.time.place.chosenPlaces
        self.sumPrice = self.price * len(cinema.kino.time.place.chosenPlaces)
    
    def __str__(self):
        data =  "Cinema: {}".format(self.cinemaName)+"\n"
        data += "Kino:   {}".format(self.kino)+"\n"
        data += "Time:   {}".format(self.time)+"\n"
        data += "Place:  {}".format(self.place)+"\n"
        data += "One ticket price:  {}".format(self.price)+"\n"
        data += "Total price:       {}".format(self.sumPrice)+"\n"
        return data