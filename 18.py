'''
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

array = [] # Ініціалізуємо масив

answer = 1 # Ініціалізуємо змінну у яку збережемо добуток

for i in range(10): # проходимо цикл 0 рзів
    x = int(input()) # ввводимо з руки число
    array.append(x) # додаємо його у масив
    if x < 0: # перевіряємо умову чи менше число 0
        answer *= x # якщо менше, то множимо на весь добуток
if answer == 1: # якщо увесь добуток рівний 1, значить від'ємних чисел не було
    print("No such elements")
else: # інакше виводимо відповідь
    print(answer)