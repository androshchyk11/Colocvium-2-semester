'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

t = False

n = int(input("Input quantity of array: "))  # Користувач вводить кількість чисел у масиві

a = int(input("Input a number: "))  # Користувач вводить числo

array = []  # Ініціалізуємо масив
maxNumbers = []

for i in range(n):  # проходимо по циклу n разів
    x = int(input())  # вводимо число з клавіатури
    array.append(x)  # додаємо це число до масиву

maxNum = array[0]  # присваюємо змінній перше значення масиву

# шукаємо максимальнен число у масиві
for i in range(n):
    if (maxNum <= array[i]):
        maxNum = array[i]

    # додаємо числа рівні максимальному у масив з найбільшими числами
for i in range(n):
    if maxNum == array[i]:
        maxNumbers.append(array[i])
# перевіряємо чи найбільше число одне та чи не перевищує задане
if len(maxNumbers) == 1 and maxNum <= a:
    t = True

print(t)
