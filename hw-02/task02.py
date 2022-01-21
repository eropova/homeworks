import random


class Appliance:
    """Класс для описания свойств и методов
    для любого товара из магазина бытовой электроники.
    Свойство acc_price - для накопления цен всех товаров в маганизе,
    acc_quantity - для накопления общего количества товаров в магазине"""

    acc_price = 0
    acc_quantity = 0

    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = 0
        self.price = 0

    def supply(self, quantity_add, price_add):
        """Метод изменяет количество и цену товара при поступлении
        и увеличивает накопительные значения"""
        self.quantity += quantity_add
        self.price = price_add
        Appliance.acc_price += self.quantity * self.price
        Appliance.acc_quantity += self.quantity

    def sell(self, quantity_del):
        """Метод уменьшает количество товара при продаже
        и изменяет накопительные значения"""
        if self.quantity < quantity_del:
            return 'нет такого количества'
        else:
            self.quantity -= quantity_del
            Appliance.acc_price -= self.price * self.quantity
            Appliance.acc_quantity -= self.quantity

    @classmethod
    def accumulate(cls):
        """Метод расчитывает среднюю цену всех товаров в магазине"""
        avg_price = cls.acc_price / cls.acc_quantity
        return f'средняя цена всех товаров составляет: {avg_price}'

    @classmethod
    def comparison(cls, item1, item2):
        """Сравнивает между собой объекты одного класса по исключительному свойству"""
        if item1.__class__ == item2.__class__:
            if item1.__class__ == Fridge:
                if item1.number_chambers == item2.number_chambers:
                    return 'товары равны по качеству'
                elif item1.number_chambers > item2.number_chambers:
                    return f'{item1.type} {item1.name} лучше {item2.type} {item2.name}'
                else:
                    return f'{item2.type} {item2.name} лучше {item1.type} {item1.name}'
            if item1.__class__ == TVSet:
                if item1.diagonal == item2.diagonal:
                    return 'товары равны по качеству'
                elif item1.diagonal > item2.diagonal:
                    return f'{item1.type} {item1.name} лучше {item2.type} {item2.name}'
                else:
                    return f'{item2.type} {item2.name} лучше {item1.type} {item1.name}'
        else:
            return 'товары из разных категорий нельзя сравнить между собой'


class Fridge(Appliance):
    """Наследник класса Appliance, для товара холодильник"""
    def __init__(self, name, manufacturer, number_chambers):
        super().__init__(name, manufacturer)
        self.type = 'refrigerator'
        self.number_chambers = number_chambers
        self.warranty = False

    def extended_warranty(self, war_cost):
        """Метод изменяет свойство товара warranty (расширенная гарантия) на True
        и увеличивает цену на % наценки за услугу"""
        self.warranty = True
        self.price += int(self.price * war_cost)
        Appliance.acc_price += self.price * war_cost * self.quantity


class TVSet(Appliance):
    """Наследник класса Appliance, для товара телевизор"""
    def __init__(self, name, manufacturer, diagonal):
        super().__init__(name, manufacturer)
        self.type = 'tv set'
        self.diagonal = diagonal
        self.add_ip_tv = False

    def ip_tv(self, ip_cost):
        """Метод изменяет свойство товара add_ip_tv (дополнительная установка ip-tv) на True
                и увеличивает цену на % наценки за услугу"""
        self.add_ip_tv = True
        self.price += int(self.price * ip_cost)
        Appliance.acc_price += self.price * ip_cost * self.quantity


shop = []
manufacturers = ['AEG', 'Bosch', 'Candy', 'Daewoo']

fridge_1 = Fridge('XTS 158', random.choice(manufacturers), random.randrange(1, 3))
fridge_2 = Fridge('ADJ 8585', random.choice(manufacturers), random.randrange(1, 3))
fridge_3 = Fridge('OOJU 9901', random.choice(manufacturers), random.randrange(1, 3))
tv_1 = TVSet('WRUD 0087k', random.choice(manufacturers), random.randrange(10, 105))
tv_2 = TVSet('LJOP 7875lk', random.choice(manufacturers), random.randrange(10, 105))
tv_3 = TVSet('FMBI a2409', random.choice(manufacturers), random.randrange(10, 105))
shop.extend([fridge_1, fridge_2, fridge_3, tv_1, tv_2, tv_3])

for item in shop:
    item.supply(random.randrange(2, 5), random.randrange(10500, 25000))

shop[2].extended_warranty(0.1)
shop[3].ip_tv(0.08)

for item in shop:
    item.sell(random.randrange(1, 2))


for i in shop:
    print(i.__dict__)

print(Appliance.accumulate())

print(Appliance.comparison(fridge_3, fridge_2))
print(Appliance.comparison(tv_1, fridge_2))
print(Appliance.comparison(tv_1, tv_3))
