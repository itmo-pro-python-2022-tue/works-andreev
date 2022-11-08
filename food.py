class Food:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__class__.count += 1

    def eat(self):
        print(f'{self.name} was eaten')

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    @staticmethod
    def anecdote():
        return 'Почему в таблице Менделеева йод есть, а зеленки нет?'

    def __str__(self):
        return f'{self.name} за {self.price} руб.'


class Drink:
    def __init__(self, name, variant, price):
        self.name = name
        self.variant = variant
        self.price = price

    def drink(self):
        print(f'{self.name} was drunk')

    def __str__(self):
        return f'{self.variant} "{self.name}" за {self.price} руб.'


# Создаём новый объект класса Food
cake = Food('Тортик', 150)
cake.eat()
print(cake)

sushi = Food('Суши', 220)
sushi.eat()
print(sushi.__str__())

print(Food.get_report())
print(cake.anecdote())
print(Food.anecdote())

latte = Drink('Латте', 'Кофе', 190)
latte.drink()
print(latte)
