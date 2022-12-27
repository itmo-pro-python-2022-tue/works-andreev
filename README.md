# Система управления кофейней

> Ради кофе можно пойти на всё. Даже на работу. © Билл Гейтс

## Описание системы

Небольшая *система* для **управления** сетью ***кофеен***.

Система ![GitHub Logo](https://camo.githubusercontent.com/b6a12909f1e31185a69a73d59208c507a992236d3230f9fc18e85058ae3d19e7/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f66617669636f6e732f66617669636f6e2e737667) предназначена для учёта товаров ~~и управления персоналом~~.

Пример работающей системы можно посмотреть [по этой ссылке](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

![Самый красивый певец всех времён и народов](https://entertainment.inquirer.net/files/2022/08/Rick-Astley.png)

## Возможности системы

* Хранение информации о товарах;
* Разделение товаров на еду и напитки;
* Работа с персоналом.

- Ещё список

+ И ещё один список

1. А это нумерованный список
2. И его второй пункт
   1. Вложенный нумерованный список
   2. Второй пункт
   3. Третий пункт
      1. Вложенный список (ещё раз) 
3. И третий пункт
   + Вложенный маркированный список
   + И его второй пункт

## Пример использования

Для более подробного описания изучите классы `Food` и `Drink`.

```python
cake = Food('Тортик', 150, 5)
sushi = Food('Суши', 220, 3)
latte = Drink('Латте', 'Кофе', 190, 10)
kvass = Drink('Хлебный', 'Квас', 70, 5)
switch = Item('Nintendo Switch', 23990, 1)

for item in cake, sushi, latte, kvass, switch:
    print(item)

print(Food.get_report())
print(Drink.get_report())

exporter = FileItemsExporter('items.txt')
exporter.export([cake, sushi, latte, kvass, switch])

table_exporter = CSVFileExporter('items.csv')
table_exporter.export([cake, sushi, latte, kvass, switch])
```

|          Название | Стоимость | Количество |
|------------------:|:---------:|:-----------|
|            Тортик |    150    | 5          |
|          **Суши** |    220    | 3          |
|             Латте |    190    | 10         |
|      Хлебный квас |    70     | 5          |
| `Nintendo Switch` |   23990   | 1          |

## Формула расчёта зарплаты

$$
ax^2 + bx + c = 0
$$

$$
\sum^n_{i=0}{\frac{1}{2^i}} = 2
$$