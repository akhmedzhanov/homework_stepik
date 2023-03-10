'''
Дан список сотрудников организации, в котором указаны их фамилии, 
имена и даты рождения. Напишите программу, которая определяет 
самого старшего сотрудника из данного списка.
'''

from datetime import datetime as dt


n = int(input('Введите количество сотрудников: ')) # n = 4 для данного теста
emp_info = {}
lst = [
    'Иван Петров 01.05.1995',
    'Петр Сергеев 29.04.1995',
    'Сергей Иванов 01.01.1996',
    'Сергей Ивановский 01.01.1996'
    ]

for i in range(len(lst)):
    f_name, l_name, d = lst[i].split()
    emp_info[f'{f_name} {l_name}'] = dt.strptime(d, '%d.%m.%Y')

oldest_emp_birthday = min(emp_info.values())
counter = 0
for key, value in emp_info.items():
    if (dt.today() - value).days == (dt.today() - oldest_emp_birthday).days:
        counter += 1
if counter > 1:
    print(oldest_emp_birthday.date().strftime('%d.%m.%Y'), counter)
else:
    print(oldest_emp_birthday.date().strftime('%d.%m.%Y'), min(emp_info, key=emp_info.get))
