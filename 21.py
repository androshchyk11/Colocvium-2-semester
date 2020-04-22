'''
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import random

sum = 0  # Ініціалізуємо змінну сума
a = [random.uniform(50, 100) for i in range(20)]  # створюємо масив за допогою генератора списку
print(a)  # виводимо масив на екран

x = int(input("Input a number: "))  # Користувач вводить число

answer = 1  # Ініціалізуємо змінну сума
for i in range(20):  # проходимо по елементам
    if a[i] < x:  # перевіряємо чи елемент масиву менший за це число
        answer *= a[i]  # домножаємо до суми

if (answer == 1):
    print("no such elements")
else:
    print(answer)  # виводимо відповідь
