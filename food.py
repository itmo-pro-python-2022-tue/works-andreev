from abc import abstractmethod


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
        else:
            raise ValueError('Cannot set negative amount of item')

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} items'


class FileItemsExporter:
    def __init__(self, filename):
        self._filename = filename

    def export(self, items):
        file = open(self._filename, 'w', encoding='utf-8')
        for item in items:
            print(item, file=file)
        file.close()


class CSVFileExporter(FileItemsExporter):
    def export(self, items):
        file = open(self._filename, 'w', encoding='utf-8')
        for item in items:
            print(item.name, item.price, item.amount, sep=',', file=file)
        file.close()


class IConsumable:
    @abstractmethod
    def consume(self):
        pass


class ICookable:
    @abstractmethod
    def cook(self):
        pass


class IBrewable:
    @abstractmethod
    def brew(self):
        pass


class Food(Item, IConsumable, ICookable):
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

    def cook(self):
        pass


class Drink(Item, IConsumable, IBrewable):
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

    def brew(self):
        pass


cake = Food('Тортик', 150, 5)
sushi = Food('Суши', 220, 3)
latte = Drink('Латте', 'Кофе', 190, 10)
kvass = Drink('Хлебный', 'Квас', 70, 5)
switch = Item('Nintendo Switch', 23990, 1)

for item in cake, sushi, latte, kvass, switch:
    print(item)

print(Food.get_report())
print(Drink.get_report())

cake.amount -= 8

exporter = FileItemsExporter('items.txt')
exporter.export([cake, sushi, latte, kvass, switch])

table_exporter = CSVFileExporter('items.csv')
table_exporter.export([cake, sushi, latte, kvass, switch])
