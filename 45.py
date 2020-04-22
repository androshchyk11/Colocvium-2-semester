'''
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''
import math

radius = int(input("radius: "))
delta = radius / 5
x = 0
i = 0

while x < 2 * radius - delta:
    x += delta
    i += 1
    h = math.sqrt(x * (2 * radius - x))
    print(f"Height of {i} prop: {h}")
