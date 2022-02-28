# Import Class
# from first_mudiol import Robot as r
# from first_mudiol import Huaman as H
from second_modul import Animal
import first_mudiol as f
print('-------robot--------')
robot = f.Robot("Sumaiya", "6 years")
robot.show_name()
robot.show_age()

print('-----human---------')
huamn=f.Huaman("kamal","4 years", 'apple')
huamn.show_name()
huamn.show_age()
huamn.show_food()

print("---animl---------")
animl = Animal("akash","5 years", "mango", "pet name")
animl.show_name()
animl.show_age()
animl.show_food()
animl.show_pet()

class Anika:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)
        print("ANIKA Class")

class Salman:
    def __init__(self,name,age):
        super().__init__(name)
        self.age =age
    def show_age(self):
        print(self.age)
        print("10 years old")

anika = Anika("Anka Sultana")
salman = Salman("salman", "12 years old")
anika.show_name()
salman.show_name()
salman.show_age()