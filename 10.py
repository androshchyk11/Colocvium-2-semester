'''
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

temperature = [20, 14, -5, 1, 23, 5, 7, -8, -7, 0]  # Ініціалізуємо масив з температурами(можна дані змінити)
answer = 0  # ініціалізуємо змінну результату

for i in range(10):  # проходимо по циклу 10 разів
    if (temperature[i] < 10):  # перевіряємо умову на від'ємність
        answer += 1  # якщо температура <10, то збільшуємо результат
print(answer)  # Виводимо відповідь
