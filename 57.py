'''
Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
Виконав студент групи КН-А Андрощук Артем Олександрович
'''

surnames = ['Андрощук', 'Антонов', 'Петров', 'Іванов']  # Створюємо масив з прізвищами
salaries = [400, 200, 320, 100]  # Створюємо масив з зарплатнею
print(surnames)
print(salaries)
difference = []  # створюємо новий масив, куди запишемо усі різниці з середньою зарплатою

# знаходимо середню зарплату
seredn = 0
for i in range(len(salaries)):
    seredn += salaries[i]
seredn /= len(salaries)
# тепер заповнюємо масив різниць віднімаючи від середньої зарплатні зарплатню працівника
for i in range(len(salaries)):
    difference.append(seredn - salaries[i])
serednSalary = abs(
    difference[0])  # будемо за допомогою цієї змінної знаходити найменше відхилення, яке беремо по модулю
indexOfAMan = 0  # індекс найменшого відхилення, щоб потім вивести прізвище
# знаходимо найменше відхилення та його індекс
for i in range(len(difference)):
    if serednSalary > abs(difference[i]):
        serednSalary = abs(difference[i])
        indexOfAMan = i
# Виводимо відповідь
print("This man has less difference from average salary:", surnames[indexOfAMan])

# Для того, щоб знайти у кого найбільша зарплата та найменша потрібно відсортувати масив із зарплатами, і відповідно до змін у ньому потрібно міняти масив
# прізвищ, адже вони пов'язані між собою
for i in range(len(salaries)):
    for j in range(0, len(salaries) - i - 1):
        if salaries[j] > salaries[j + 1]:
            salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
            surnames[j], surnames[j + 1] = surnames[j + 1], surnames[j]
print()
print("These man have the biggest salary: ")
print(surnames[-1], " ", surnames[-2])
# Видаляємо прізвище та зарплатню того, хто заробляє найменше
print()
salaries.remove(salaries[0])
surnames.remove(surnames[0])
print(surnames)
print(salaries)
