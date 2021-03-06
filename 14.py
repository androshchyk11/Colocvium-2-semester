'''
Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

import math # Імпортуємо бібліотеку для того, щоб використати степінь

array = [] # Ініціалізуємо масив

for i in range(1, 11, 1): # проходимо циклом з 1 по (11 не включно) з кроком 1
    x = (9.8 * math.pow(i, 2)) / 2 # рахуємо по формулі відстань при вільному падінні
    array.append(x) # додаємо це значення до масиву
print(array) # виводим його на екран
