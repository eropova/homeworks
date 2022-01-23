from random import choice


class Skier:
    """Класс для описания свойств лыжника:
    name - имя, age возраст"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def go(self, time):
        """Метод для для спуска лыжника"""
        time = Moving.time
        for _i in range(time):
            gals = choice(list(Moving.speed.keys()))
            Moving.distance_pass += Moving.speed[gals]
            Moving.directions.append(gals)
        return (f"За {Moving.time} секунд лыжник {self.name} проехал {Moving.distance_pass} метров "
                f"по следующим направлениям:\n" + "\n".join(Moving.directions))


class Moving:
    """Класс для описания свойств спуска:
    speed - скорости различных направлений спуска,
    distance_pass - пройденная дистанция,
    directions - список пройденных направлений,
    time - время спуска"""
    speed = {'east': 1, 'south': 5, 'west': 1}
    distance_pass = 0
    directions = []
    time = 17


def main():
    skier1 = Skier('John', 99)
    print(skier1.go(Moving()))


if __name__ == "__main__":
    main()
