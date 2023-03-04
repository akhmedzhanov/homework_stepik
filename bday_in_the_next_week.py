'''
Дан список сотрудников организации, в котором указаны их фамилии, 
имена и даты рождения. Напишите программу, которая определяет самого 
молодого сотрудника, празднующего свой день рождения в течение ближайших 
семи дней от указанной даты.
'''

from datetime import datetime as dt, timedelta as td, date

now_date = dt.strptime(input(), '%d.%m.%Y') + td(days=1)
#now_date = dt.strptime('14.11.2021', '%d.%m.%Y') + td(days=1)
n = int(input())
#n = 3
lst = [input() for _ in range(n)]
#lst = [
#    'Иван Петров 16.11.1995',
#    'Петр Сергеев 14.11.1997',
#    'Сергей Романов 17.11.1994'
#    ]
b_dates = {}
birthday_men = {}
next_week_dates = []

step = 86400 #sec*min*hours
for d in range(int(now_date.timestamp()), int((now_date + td(days=7)).timestamp()), step):
    next_week_dates.append(dt.fromtimestamp(d).date())

for i in range(len(lst)):
    f_name, l_name, d = lst[i].split()
    new_date = dt.strptime(d, '%d.%m.%Y')
    b_dates[new_date] = f'{f_name} {l_name}'
    if date(now_date.year, new_date.month, new_date.day) in next_week_dates or date(now_date.year + 1, new_date.month, new_date.day) in next_week_dates:
        birthday_men[f'{f_name} {l_name}'] = dt.timestamp(new_date)


if birthday_men:
    print(max(birthday_men.items(), key=lambda x: x[1])[0])
else:
    print('Дни рождения не планируются')
