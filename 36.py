'''
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

array = []  # Ініціалізуємо масив

for i in range(10):  # проходимо по циклу n разів
    x = int(input())  # вводимо число з клавіатури
    array.append(x)  # додаємо це число до масиву

sum = 0  # Ініціалізуємо змінну сума
for i in range(10):  # проходимо 10 разів по циклу
    if array[i] > 0:  # перевіряємо чи число більше 0
        sum += array[i]  # додаємо до суми
print(sum)