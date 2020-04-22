'''
Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

n = int(input("Input quantity of array: "))  # Користувач вводить кількість чисел у масиві

array = []  # Ініціалізуємо масив

for i in range(n):  # проходимо по циклу n разів
    x = int(input())  # вводимо число з клавіатури
    array.append(x)  # додаємо це число до масиву
max = array[0]  # Ініціалізуємо змінну у якій будемо хранити максимальне число
helper = []
# знаходимо максимальне число по парним номерам
for i in range(0, n, 2):
    if array[i] > max:
        max = array[i]

print("Max number - ", max)  # Виводимо максимальне число на екран

# додаємо усі максимальні елементи у масив
for i in range(n):
    if max == array[i]:
        helper.append(max)
# еревіряємо к-сть елементів у масиві з максимальними числами
if len(helper) == 1:
    print("There is only 1 maximal element")
else:
    print("It`s not the only maximum number")
