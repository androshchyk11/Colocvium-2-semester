'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

# вводимо число а та перевіряємо чи воно натуральне
while True:
    a = int(input("a = "))
    if a > 0:
        break
# вводимо число b та перевіряємо чи воно натуральне
while True:
    b = int(input("b = "))
    if b > 0:
        break

w = False

n = int(input("Input quantity of array: "))  # Користувач вводить кількість чисел у масиві

array = []  # Ініціалізуємо масив

for i in range(n):  # проходимо по циклу n разів
    x = int(input())  # вводимо число з клавіатури
    array.append(x)  # додаємо це число до масиву
for i in range(n): # проходимо по циклу n разів
    if (array[i] % a == 0 and array[i] % b != 0): # перевіряємо умову задачі
        w = True
print(w)