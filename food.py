class Item:
    count = 0

    def __init__(self, name, price, amount):
        self.name = name
        self._price = price
        self._amount = amount
        self.__class__.count += amount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 10:
            self._price = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self.__class__.count += value - self.__class__.count
            self._amount = value

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} items'


class Food(Item):
    def __init__(self, name, price, amount=1):
        super().__init__(name, price, amount)

    def consume(self):
        if self._amount > 0:
            print(f'{self.name} was eaten')
            self._amount -= 1
            self.__class__.count -= 1
        else:
            print(f'There is no {self.name} left')

    @staticmethod
    def anecdote():
        return 'Почему в таблице Менделеева йод есть, а зеленки нет?'

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    def __str__(self):
        return f'{self.name} за {self._price} руб. ({self._amount} шт.)'


class Drink(Item):
    def __init__(self, name, variant, price, amount=1):
        super().__init__(name, price, amount)
        self.variant = variant

    def consume(self):
        print(f'{self.name} was drunk')

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} drinks'

    def __str__(self):
        return f'{self.variant} "{self.name}" за {self.price} руб. ({self._amount} шт.)'


cake = Food('Тортик', 150, 5)
sushi = Food('Суши', 220, 3)
latte = Drink('Латте', 'Кофе', 190, 10)
kvass = Drink('Хлебный', 'Квас', 70, 5)

for item in cake, sushi, latte, kvass:
    print(item)

print(Food.get_report())
print(Drink.get_report())
