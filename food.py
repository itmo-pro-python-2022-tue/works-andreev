class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def eat(self):
        print(f'{self.name} was eaten')

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

latte = Drink('Латте', 'Кофе', 190)
latte.drink()
print(latte)
