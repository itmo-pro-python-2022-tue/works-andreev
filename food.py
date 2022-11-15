class Food:
    count = 0

    def __init__(self, name, price, amount=1):
        self.name = name
        self.price = price
        self.__amount = amount
        self.__class__.count += amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self.__class__.count += value - self.__class__.count
            self.__amount = value

    def consume(self):
        if self.__amount > 0:
            print(f'{self.name} was eaten')
            self.__amount -= 1
            self.__class__.count -= 1
        else:
            print(f'There is no {self.name} left')

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    @staticmethod
    def anecdote():
        return 'Почему в таблице Менделеева йод есть, а зеленки нет?'

    def __str__(self):
        return f'{self.name} за {self.price} руб. ({self.__amount} шт.)'


class Drink:
    def __init__(self, name, variant, price):
        self.name = name
        self.variant = variant
        self.price = price

    def consume(self):
        print(f'{self.name} was drunk')

    def __str__(self):
        return f'{self.variant} "{self.name}" за {self.price} руб.'


# Создаём новый объект класса Food
cake = Food('Тортик', 150)
cake.consume()
cake.consume()
print(cake)

sushi = Food('Суши', 220)
sushi.consume()
print(sushi.__str__())

print(Food.get_report())
print(cake.anecdote())
print(Food.anecdote())

latte = Drink('Латте', 'Кофе', 190)
latte.consume()
print(latte)

for item in cake, sushi, latte:
    item.consume()
