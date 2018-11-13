from cinema import Cinema
from DB import DB
from ticket import Ticket
from user import User

def buyTicket(user):
    db = DB()
    data = db.select('Cinemas', ['id', 'name'])
    # Choose cinema
    while True:
        print()
        for dt in data:
            print(dt[0], dt[1])
        request = input("\n<> Choose one of these cinemas:\n>> ")
        if request == 'back':
            return False, "Back"
        try:
            request = int(request)
        except:
            print('\n!!! Please, enter INTEGER number!')
            continue
        if request < 1 or request > len(data):
            print("\n!!! Сhoose cinemas that do not exceed the number of cinemas")
            continue
        cinema = Cinema(data[request-1][0], data[request-1][1])
        # Choose movie
        while True:
            print()
            for kino in cinema.listKino:
                print(kino["id"], kino["name"])
            request = input("\n<> Choose the movie you want to watch:\n>> ")
            if request == "back":
                break
            try:
                request = int(request)
            except:
                print('\n!!! Please, enter INTEGER number!')
                continue
            if request < 1 or request > len(cinema.listKino):
                print("\n!!! Choose films that do not exceed the amount of film")
                continue
            cinema.setChosenKino(request-1)
            # Choose time
            while True:
                print("\n","ID","Time","Price")
                time_id = 1
                for time in cinema.getTimes():
                    print(time_id, time['time'], time['price'])
                    time_id += 1
                request = input("\n<> Choose one of these times:\n>> ")
                if request == "back":
                    break
                try:
                    request = int(request)
                except:
                    print('\n!!! Please, enter INTEGER numbers!')
                    continue
                if request < 1 or request > time_id:
                    print("\n!!! Select a time that does not exceed the ID time")
                    continue
                cinema.setChosenTime(cinema.getTimes()[request-1]['id'])
                # Choose place
                placeArr = []
                while True:
                    print()
                    for place in cinema.getPlaces():
                        if place['status'] == 0:
                            print(place['place'], end="  ")
                            placeArr.append(place['place'])
                    request = input("\n<> Select one or more places (with a space):\n>> ")
                    if request == "back":
                        break
                    try:
                        request = [int(i) for i in request.split()]
                    except:
                        print('\n!!! Please, enter INTEGER numbers!')
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
                        return True, cinema

def main():
    print("\nWelcome to the ticketing service.")
    user = User()
    request = None
    while True:
        while True:
            checkIn = False
            isCreated = False
            print("\n<> 1. Sing In\n<> 2. Create Account\n<> 3. Turn off the system")
            request = input(">> ")
            if request == "3":
                user = User()
                print("\nGoodbye. We'll be waiting for you!")
                break
            # sing in
            elif request == "1":
                login = input("Your login:\n>> ")
                password = input("Your password:\n>> ")
                if user.checkUser(login, password):
                    checkIn = True
            # registration
            elif request == "2":
                login = input("Your login:\n>> ")
                password = input("Your password:\n>> ")
                name = input("What is your name:\n>> ")
                surname = input("What is your surname:\n>> ")
                if not user.createUser(login, password, name, surname):
                    isCreated = True
                else:
                    break
            if checkIn:
                break
            elif isCreated:
                print("\n!!! Choose another login. This already exists")
            else:
                print("\n!!! Wrong login or password. Try again\n")
        if request == "3":
            break
        isLogout = False
        while True:
            print("\n<> 1. Buy ticket\n<> 2. My ticket\n<> 3. Log out")
            request = input(">> ")
            if request == "3":
                user = User()
                isLogout = True
                break
            elif request == "1":
                buy = buyTicket(user)
                if not buy[0]:
                    continue
                cinema = buy[1]
                ticket = Ticket()
                ticket.setTicket(cinema)
                print("\nYour ticket:\n{}".format(ticket))
                user.setTicket(ticket)
            elif request == "2":
                print()
                if user.myTickets():
                    for item in range(0, len(user.myTickets())):
                        print(user.myTickets()[item])
                        if item != len(user.myTickets())-1:
                            print("-----------------------------")
                else:
                    print("!!! Empty\n")
        if isLogout:
            continue
        

if __name__ == '__main__':
	main()