class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def printName(self):
        return self.name+" "+self.surname

# Наследование - наследовать данные и функциональность некоторого 
# существующего типа, способствуя повторному использованию компонентов

class Info(Person):
    def __init__(self, name, surname, age):
        Person.__init__(self, name, surname)
        self.age = age
    def printInfo(self):
        return self.printName()+" "+self.age
    # эту функцию я использовал для примера полимарфизма
    def printSex(self):
        return "This method is in Info class"

# полиморфизм — это способность обьекта использовать методы производного класса
class asd(Info):
    def __init__(self, name, surname, age, sex):
        Info.__init__(self, name, surname, age)
        self.sex = sex
    def printSex(self):
        return self.printInfo()+", sex: "+self.sex

person = Person("Maksat", "Nurtai")
info = Info("Janel", "Drewis", "20")
temp = asd("Jhon", "Martin", "26", "male")
print(person.printName())
print(info.printInfo())
print(temp.printSex())