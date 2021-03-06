'''
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import random

sum = 0  # Ініціалізуємо змінну сума
a = [random.uniform(100, 200) for i in range(20)]  # створюємо масив за допогою генератора списку
print(a)  # виводимо масив на екран

sum = 0 # Ініціалізуємо змінну сума
for i in range(1, 20, 2): # проходимо по непарним номерам елементів
    sum += a[i] # додаємо до суми
print(sum) # виводимо відповідь
