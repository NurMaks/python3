from controller.database import DB

class User:
    def __init__(self):
        self.id = None
        self.login = None
        self.password = None
        self.name = None
        self.db = DB()
    
    def checkUser(self, login, password):
        user = None
        try:
            user = self.db.select("Users", "*", "login='"+str(login)+"';")
        except:
            return False
        if user:
            if user[0][1]==login and user[0][2]==password:
                self.id = int(user[0][0])
                self.name = user[0][3]
                self.surname = user[0][4]
                self.login = user[0][1]
                self.password = user[0][2]
                return True
        return False

    
    def createUser(self, login, password, name, surname):
        user = None
        try:
            user = self.db.select("Users", "*", "login='"+str(login)+"';")
        except:
            pass
        if user:
            return False
        user = self.db.select("Users", "*")
        if user:
            self.id = int(user[len(user)-1][0])+1
        else:
            self.id = 1
        self.name = name
        self.login = login
        self.password = password
        self.surname = surname
        self.db.insertUser(self.id, login, password, name, surname)
        return True
        