from cinema import Cinema
from DB import DB
from colorama import Fore
import sys
from ticket import Ticket


def printTicket(cinema):
    ticket = Ticket(cinema)
    print("\nYour ticket:\n{}".format(ticket))   
    systemCheck("end")

def systemCheck(request):
    if request == "end" or request == "break" or request == "close":
        return sys.exit(0)

def main():
    print()
    print("Welcome to the ticketing service.\n")
    db = DB()
    data = db.select('Cinema', ['cinema_id', 'cinema'])
    print("List of cinemas (ID):")
    request = ""
    ch = False
    while True:
        for dt in data:
            print(dt[0], dt[1])
        request = input("\nChoose one of these cinemas:\n>> ")
        systemCheck(request)
        try:
            request = int(request)
        except:
            print('<> Please, enter INTEGER number!')
            continue
        if request < 1 or request > len(data):
            print("<> Сhoose cinemas that do not exceed the number of cinemas")
            continue
        #print(data[0][request-1], data[1][request-1])
        cinema = Cinema(data[request-1][0], data[request-1][1])
        for kino in cinema.listKino:
            print(kino["id"], kino["name"])
        while True:
            request = input("\nChoose the movie you want to watch:\n>> ")
            if request == "back":
                break
            systemCheck(request)
            try:
                request = int(request)
            except:
                print('<> Please, enter INTEGER number!')
                continue
            if request < 1 or request > len(cinema.listKino):
                print("<> Choose films that do not exceed the amount of film")
                continue
            cinema.setChosenKino(request)

            print("ID","Time","Price")
            for time in cinema.getTimes():
                print(time['id'], time['time'], time['price'])
            while True:
                request = input("\nChoose one of these times:\n>> ")
                systemCheck(request)
                if request == "back":
                    break
                try:
                    request = int(request)
                except:
                    print('<> Please, enter INTEGER numbers!')
                    continue
                if request < cinema.getTimes()[0]['id'] or request > cinema.getTimes()[len(cinema.getTimes())-1]['id']:
                    print("<> Select a time that does not exceed the ID time")
                    continue
                cinema.setChosenTime(request)

                placeArr = []
                for place in cinema.getPlaces():
                    if place['status'] == 0:
                        print(place['place'], end="  ")
                        placeArr.append(place['place'])
                while True:
                    systemCheck(request)
                    if request == "back":
                        break
                    request = input("\nSelect one or more places (with a space):\n>> ")
                    try:
                        request = [int(i) for i in request.split()]
                    except:
                        print('<> Please, enter INTEGER numbers!')
                        continue
                    ch = True
                    for req in request:
                        if not req in placeArr:
                            ch = False
                            break
                    if not ch:
                        print("<> Please select only free places!")
                        continue
                    else:
                        cinema.setChosenPlaces(request)
                        print("Perfect thank you!")
                    printTicket(cinema)

if __name__ == '__main__':
	main()