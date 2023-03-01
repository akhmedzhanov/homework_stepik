'''
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого старшего сотрудника из данного списка.
'''

from datetime import datetime as dt, timedelta as tm


n = int(input())
emp_info = {}
lst = [
    'Иван Петров 01.05.1995',
    'Петр Сергеев 29.04.1995',
    'Сергей Иванов 01.01.1996'
    ]



for i in range(len(lst)):
    f_name, l_name, d = lst[i].split()
    emp_info[f'{f_name} {l_name}'] = dt.strptime(d, '%d.%m.%Y')

print(emp_info)
