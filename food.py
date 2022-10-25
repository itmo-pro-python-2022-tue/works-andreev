class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def eat(self):
        print(f'{self.name} was eaten')


# Создаём новый объект класса Food
cake = Food('Тортик', 150)
cake.eat()
print(cake.name, cake.price)

sushi = Food('Суши', 220)
sushi.eat()
print(sushi.name, sushi.price)
