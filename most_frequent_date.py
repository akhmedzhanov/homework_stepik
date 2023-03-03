'''
Дан список сотрудников организации, в котором указаны их фамилии, 
имена и даты рождения. Напишите программу, которая определяет 
самого старшего сотрудника из данного списка.
'''

from datetime import datetime as dt


n = int(input('Введите количество сотрудников: ')) # n = 5 для данного теста
lst = [
    'Иван Петров 01.05.1995',
    'Петр Сергеев 29.04.1995',
    'Сергей Романов 01.01.1996',
    'Роман Григорьев 01.01.1996',
    'Григорий Иванов 01.05.1995'
    ]
frequence_dates = {}

for i in range(len(lst)):
    f_name, l_name, d = lst[i].split()
    frequence_dates[dt.strptime(d, '%d.%m.%Y')] = frequence_dates.get(dt.strptime(d, '%d.%m.%Y'), 0) + 1

for key, value in sorted(frequence_dates.items()):
    if value > 1:
        print(key.date().strftime('%d.%m.%Y'))
    elif all(value == 1 for value in frequence_dates.values()):
            print(key.date().strftime('%d.%m.%Y'))


