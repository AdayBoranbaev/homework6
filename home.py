#-----------1----------------------
from time import sleep
class TrafficLight:
    __color = "Цвета"

    def running(self):
        while True:
            print("Сейчас загорится красный ")
            sleep(7)
            print("Сейчас загорится желтый ")
            sleep(2)
            print("Сейчас загорится зеленый ")
            sleep(7)

trafficlight = TrafficLight()
trafficlight.running()



#-------------2----------------------

class Road:
    def __init__(self, l, w, m, p):
        self._length = l
        self._width = w
        self._mass = m
        self._pol = p

    def result(self):
        return f"{self._length} * {self._width} * {self._mass}* {self._pol} =" \
                f"{(self._length * self._width * self._mass * self._pol) / 1000}"

    road_n = Road(5000, 20, 25, 5)
    print(road_n.result)



#---------------3------------------------

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def rename(self):
        return f"{self.name} {self.surname}"

    def profit(self):
        return sum(self._income.values())

result = Position("Aday", "Boranbaev", "Worker", 250000, 20000)
print(result.rename())
print(result.income)
print(result.profit())

#------------4-----------------------------

#------------5-----------------------------

class Stationery:
    def __init__(self, title= "Что-то нарисуй"):
        self.title = title
    def draw(self):
        print(f"Начало {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Начните рисовать с {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Начните рисовать с {self.title} карандашом ")

class Marker(Stationery):
    def draw(self):
        print(f"Начните рисовать с {self.title} маркером")

result = Stationery()
pen = Pen("Kan")
pencil = Pencil("Troika")
marker = Marker("CIT")

subjects = [result, pen, pencil, marker]

for i in subjects:
    i.draw()