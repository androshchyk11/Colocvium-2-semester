'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import random

sum = 0  # Ініціалізуємо змінну сума
a = [random.randint(100, 200) for i in range(20)]  # створюємо масив за допогою генератора списку
print(a)  # виводимо масив на екран
for i in range(20):  # проходимо по елементам масиву
    if (a[i] % 2 == 0):  # перевіряємо чи елемент масиву парний
        sum += a[i]  # якщо парний, то додаємо до суми

print(sum)