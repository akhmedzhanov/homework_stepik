'''
Дан список сотрудников организации, в котором указаны их фамилии, 
имена и даты рождения. Напишите программу, которая определяет самого 
молодого сотрудника, празднующего свой день рождения в течение ближайших 
семи дней от указанной даты.
'''

from datetime import datetime as dt, timedelta as td, date

now_date = dt.strptime('14.11.2021', '%d.%m.%Y') + td(days=1)
n = 3
lst = [
    'Иван Петров 16.11.1995',
    'Петр Сергеев 14.11.1997',
    'Сергей Романов 17.11.1994'
    ]
b_dates = {}

for i in range(len(lst)):
    f_name, l_name, d = lst[i].split()
    b_dates[dt.strptime(d, '%d.%m.%Y')] = f'{f_name} {l_name}'

next_week_temp = []
step = 86400 #sec*min*hours
for d in range(int(now_date.timestamp()), int((now_date + td(days=7)).timestamp()), step):
    next_week_temp.append(dt.fromtimestamp(d).date())

flag = True
for d in sorted(b_dates, reverse=True):
    if date(now_date.year, d.month, d.day) in next_week_temp:
        print(b_dates[d])
        flag = False
        break
if flag:
    print('Дни рождения не планируются')
