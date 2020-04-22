'''
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import random

sum = 0  # Ініціалізуємо змінну сума
a = [random.randint(150, 300) for i in range(20)]  # створюємо масив за допогою генератора списку
print(a)  # виводимо масив на екран

seredn = 0  # Ініціалізуємо змінну у яку будемо записуваати середнє значення

for i in range(20):  # проходимо по циклу 20 разів
    seredn += a[i]  # додаємо усі значення масиву
seredn = seredn / 20  # ділимо на 20, отримуємо середнє значення

for i in range(20):  # проходимо по елементам масиву
    if (a[i] < seredn):  # перевіряємо чи елемент масиву менший ніж середнє значення
        sum += a[i]  # якщо парний, то додаємо до суми

print(sum)
