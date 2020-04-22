'''
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import random

answer = 1  # Ініціалізуємо змінну результат
a = [random.randint(10, 50) for i in range(15)]  # створюємо масив за допогою генератора списку
print(a)  # виводимо масив на екран
for i in range(15):  # проходимо по елементам масиву
    if (a[i] % 7 == 0):  # перевіряємо чи елемент масиву ділиться націло на 7
        answer *= a[i]  # якщо парний, то домножаємо до результату

if answer == 1:  # якщо відповідь рівна 1, то таких чисел не було
    print("There is no such numbers")
else:  # інакше виводимо відповідь
    print(answer)