# Сначала импортируются стандартные модули
import random
import os
# Потом внешние
import requests
# Потом свои
import food

# Вот так никогда не делайте
# import random, os, requests, food

# Но импортировать разные части
# одного модуля нужно через запятую
from math import sin, cos

# А вот так не очень хорошо
from math import gcd
from math import lcm


# Классы именуются в PascalCase
class StudyCourse:
    # Поля и методы соблюдают правила
    # для переменных и функций
    def __init__(self, course_name):
        self.course_name = course_name

    # Методы желательно разделять одной строкой
    def get_name(self):
        return self.course_name


# Названия функций также в snake_case
def get_sum(a, b):
    return a + b


# Между функциями и после последней функции
# должно быть 2 пустых строки
def greet():
    print('Hi!')


# snake_case, правильно
number_of_items = 0

# camelCase, не рекомендуется, но можно
numberOfItems = 0

# PascalCase, неправильно
NumberOfItems = 0

# Что-то страшное, неправильно
Number_Of_Items = 0

# Константы набираются ЗАГЛАВНЫМИ_БУКВАМИ
MAGIC_NUMBER = 3.14159265

a, b = 9, 5
# Вот так не совсем правильно, поскольку
# у сильных операций лучше не ставить пробелы
f = (a ** 2 + b ** 3) / 5
# Вот так лучше
f = (a**2 + b**3) / 5

# Пробелы после открывающей скобки
# и перед закрывающей не нужны
data = [ 5, 8, 13, 21 ]
s = { 3, 5, 7, 2, 1, 0 }
# Вот так нормально
data = [5, 8, 13, 21]
s = {3, 5, 7, 2, 1, 0}

# Проверку на пустоту лучше делать не через длину ...
if len(data) > 0:
    print('Non-empty')

# ... а вот так
if data:
    print('Non-empty')

result = a > b
# Логическую переменную сравнивать вот так не стоит
if result == True:
    print('OK')

# Лучше вот так
if result:
    print('OK')


# Если в проекте уже есть свой стиль кода, не нарушайте его :)
