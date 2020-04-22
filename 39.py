'''
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

temperature = [1, 6, -6, 2, 4, -3, -6, 5, 4, 1]
falls = [30, 15, 12, 3, 12, 10, 15, 20, 14, 11]

united = list(zip(temperature, falls))

snow = 0
rain = 0
for i in range(10):
    if united[i].__getitem__(0) >= 0:
        rain += united[i].__getitem__(1)
    else:
        snow += united[i].__getitem__(1)
print("snow falled - ", snow)
print("rain falled - ", rain)
