'''
Знайти кількість парних елементів одновимірного масиву.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

n = int(input("Input quantity of array: ")) # Користувач вводить кількість чисел у масиві

array = [] # Ініціалізуємо масив

answer = 0 # Ініціалізуємо змінну яка підрахує к-сть парних чисел

for i in range(n): # проходимо по циклу n разів
    x = int(input()) # вводимо число з клавіатури
    array.append(x) # додаємо це число до масиву
    if (x % 2 == 0): # перевіряємо його на парність
        answer += 1 # збільшуємо лічильник, якщо парне
print("Pair numbers in array - ", answer) # виводимо відповідь