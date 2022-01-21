from random import choice


class Skier:
    """Класс для описания свойств лыжника:
    name - имя, age возраст, on_track - позиция на трассе, по умолчанию False"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.on_track = False

    def get_ready(self):
        """Метод перемещает лыжника на стартовую позицию для спуска"""
        self.on_track = True

    def set_moving(self, moving):
        """Метод для связи объекта с объектом класса Moving"""
        self.moving = moving


class Moving:
    """Класс для описания свойств спуска:
    speed - скорости различных направлений спуска,
    distance_pass - пройденная дистанция,
    directions - список пройденных направлений"""
    speed = {'east': 1, 'south': 5, 'west': 1}
    distance_pass = 0
    directions = []

    def __init__(self, skier, time):
        self.skier = skier
        skier.set_moving(self)
        self.time = time

    def go(self):
        """Метод для для спуска лыжника"""
        for i in range(self.time):
            gals = choice(list(Moving.speed.keys()))
            Moving.distance_pass += Moving.speed[gals]
            Moving.directions.append(gals)
        return (f"За {self.time} секунд лыжник {self.skier.name} проехал {Moving.distance_pass} метров "
               f"по следующим направлениям:\n" + "\n".join(Moving.directions))


def main():
    person_name = input('Напишите имя: \n')
    person_age = int(input('Напишите возраст: \n'))
    person_time = int(input('Напишите время спуска: \n'))
    skier1 = Skier(person_name, person_age)
    skier1.get_ready()
    #skier1.get_ready()
    moving1 = Moving(skier1, person_time)
    if skier1.on_track:
        print(moving1.go())
    else:
        print('для спуска поднимитесь на гору')

if __name__ == "__main__":
    main()
