class Robot:
    """This is robot class Here, Here show name and age"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


class Huaman(Robot):
    def __init__(self, name, age, food):
        # self.name = name
        # self.age =age
        super().__init__(name,age)
        self.food = food

    # def show_name(self):
    #     print(self.name)
    #
    # def show_age(self):
    #     print(self.age)

    def show_food(self):
        print(self.food)
