'''З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

temperature = int(input("Input temperature: "))
decrease = int(input("Input decrease per hour: "))

for i in range(8, 21):
    temperature -= decrease
    if temperature < 0:
        print(f"At {i} o`clock temperature decreased above 0!")
        break
