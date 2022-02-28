class Anika:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)
        print("ANIKA Class")

    class Salman():
        def __init__(self,name,age):
            # super().__init__(name)
            self.name = name
            self.age =age

        def show_name(self):
            print(self.name)

        def show_age(self):
            print(self.age)
            print("10 years old")

anika = Anika("Anka Sultana---------")
salman =Anika.Salman("salman-----", "12 years old")
anika.show_name()
salman.show_name()
# salman.show_age()
anika.Salman.show_age()