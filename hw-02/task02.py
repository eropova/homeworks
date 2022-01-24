class Appliance:
    """Класс для описания свойств и методов
    для любого товара из магазина бытовой электроники.
    Свойство acc_price - для накопления цен всех товаров в магазине"""

    acc_price = []
    acc_quantity = []

    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = 0
        self.price = 0

    def supply(self, quantity_add, price_add):
        """Метод изменяет количество и цену товара при поступлении"""
        self.quantity += quantity_add
        self.price = price_add
        self.__class__.acc_price.append(self.price * self.quantity)
        self.__class__.acc_quantity.append(self.quantity)

    def sell(self, quantity_del):
        """Метод уменьшает количество товара при продаже"""
        if self.quantity < abs(quantity_del):
            print('нет такого количества')
        else:
            self.quantity -= quantity_del


class Fridge(Appliance):
    """Наследник класса Appliance, для товара холодильник"""
    def __init__(self, name, manufacturer, number_chambers):
        super().__init__(name, manufacturer)
        self.type = 'refrigerator'
        self.number_chambers = number_chambers
        self.warranty = False

    def extended_warranty(self):
        """Метод изменяет свойство товара warranty (расширенная гарантия) на True"""
        self.warranty = True

    def __eq__(self, other):
        return self.number_chambers == other.number_chambers

    # def __gt__(self, other):
    #     return self.number_chambers == other.number_chambers
    # def __lt__(self, other):
    #     return self.number_chambers == number_chambers.warranty


class TVSet(Appliance):
    """Наследник класса Appliance, для товара телевизор"""
    def __init__(self, name, manufacturer, diagonal):
        super().__init__(name, manufacturer)
        self.type = 'tv set'
        self.diagonal = diagonal
        self.add_ip_tv = False

    def ip_tv(self):
        """Метод изменяет свойство товара add_ip_tv (дополнительная установка ip-tv) на True"""
        self.add_ip_tv = True

    def __eq__(self, other):
        return self.diagonal == other.diagonal
    # def __gt__(self, other):
    #     return self.diagonal == other.diagonal
    # def __lt__(self, other):
    #     return self.diagonal == other.diagonal


shop = []
manufacturers = ['AEG', 'Bosch', 'Candy', 'Daewoo']

fridge_1 = Fridge('XTS 158', manufacturers[0], 2)
fridge_2 = Fridge('ADJ 8585', manufacturers[1], 1)
fridge_3 = Fridge('OOJU 9901', manufacturers[2], 2)
tv_1 = TVSet('WRUD 0087k', manufacturers[3], 32)
tv_2 = TVSet('LJOP 7875lk', manufacturers[0], 45)
tv_3 = TVSet('FMBI a2409', manufacturers[1], 32)
shop.extend([fridge_1, fridge_2, fridge_3, tv_1, tv_2, tv_3])

units = [2, 3, 2, 4, 5, 4]
prices = [21100, 13200, 24400, 34500, 55500, 24900]

for i in range(len(shop)):
    shop[i].supply(units[i], prices[i])


shop[2].extended_warranty()
shop[3].ip_tv()

for item in shop:
    item.sell(1)

for i in shop:
    print(i.__dict__)

print("Средняя цена товаров в магазине составляет: ", sum(Appliance.acc_price) / sum(Appliance.acc_quantity))

print(fridge_3 == fridge_2)
print(fridge_3 == fridge_1)
print(tv_1 == tv_3)
print(tv_1 == tv_2)
