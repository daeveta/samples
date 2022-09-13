import time


class Auto:

    def __init__(self, weight, color, brand='Audi', age=3, model='a1'):
        self.brand = brand
        self.age = age
        self.color = color
        self.model = model
        self.weight = weight

    def move(self):
        print('move!')

    @staticmethod
    def stop():
        print('stop!')

    def birthday(self):
        self.age += 1
        print(self.age)


class Truck(Auto):

    def __init__(self, weight, color, max_load, brand='Audi', age=3, model='a1'):
        super().__init__(weight, color, brand, age, model)
        self.brand = brand
        self.age = age
        self.color = color
        self.model = model
        self.weight = weight
        self.max_load = max_load

    def move(self):
        print('attention!')
        super().move()

    def load(self):
        print('LOAD')


class Car(Auto):

    def __init__(self, weight, color, max_speed, brand='Audi', age=3, model='a1'):
        super().__init__(weight, color, brand, age, model)
        self.brand = brand
        self.age = age
        self.color = color
        self.model = model
        self.weight = weight
        self.max_speed = max_speed

    def move(self):
        print('move')
        print('max speed is', self.max_speed)


auto1 = Auto(3, 'black', 'Audi', 6, 'a1')
auto2 = Truck(3, 'black', 4, 'Audi', 8, 'm1')
auto3 = Truck(6, 'white', 5, 'BMW', 7, 'm3')
auto4 = Car(7, 'black', 2, 'Mercedes', 9, 'benz')
auto5 = Car(2, 'white', 9, 'Citroen', 3, '3')

auto1.move()
auto1.stop()
auto1.birthday()

auto2.move()

time.sleep(1)
auto2.load()
time.sleep(1)

time.sleep(1)
auto3.load()
time.sleep(1)

auto4.move()
auto5.move()
