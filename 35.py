'''
Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

array = []  # Ініціалізуємо масив
n = int(input("Input quantity of array: "))  # Користувач вводить кількість чисел у масиві

for i in range(n):  # проходимо по циклу n разів
    x = int(input())  # вводимо число з клавіатури
    array.append(x)  # додаємо це число до масиву

copyOfArray = array.copy() # Створюємо копію масиву
copyOfArray.sort() # сортуємо по зростанню копію
copyOfArray = list(reversed(copyOfArray)) # повертаємо навпаки копію
if array == copyOfArray: # порівнюємо з розвернутою копією, якщо масиви однакові, то визідний масив упорядкований по спаданню
    print("Yes, elements sorted by decrease")
else:
    print("No, elements are not sorted by decrease")
