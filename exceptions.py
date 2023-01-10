def divide(a, b):
    return a / b


items = None

try:
    items = open('items.txt', 'r', encoding='utf-8')
    print(items.read())

    # "31 22" -> ["31", "22"] -> [31, 22]
    x, y = [int(x) for x in input().split()]
    print(divide(x, y))
except ZeroDivisionError as e:
    print('Деление на 0')
    print(e)
except (ValueError, TypeError) as e:
    print('Ошибка ввода')
    print(e)
else:
    print('Выполнили try без ошибок')
finally:
    print('Закрываем файл')
    items.close()
