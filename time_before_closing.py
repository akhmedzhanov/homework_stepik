'''
Напишите программу, которая принимает на вход текущие дату и время
и определяет количество минут, оставшееся до закрытия магазина
'''

from datetime import datetime as dt

schedule = {
    0: ['9:00', '21:00'],
    1: ['9:00', '21:00'],
    2: ['9:00', '21:00'],
    3: ['9:00', '21:00'],
    4: ['9:00', '21:00'],
    5: ['10:00', '18:00'],
    6: ['10:00', '18:00']
    }

cur_dt = dt.strptime(input('Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: '), '%d.%m.%Y %H:%M')
cur_weekday, cur_time = cur_dt.weekday(), cur_dt.time()

if dt.strptime(schedule[cur_weekday][0], '%H:%M').time() <= cur_time < dt.strptime(schedule[cur_weekday][1], '%H:%M').time():
    end_of_work_today = dt.combine(cur_dt.date(), dt.strptime(schedule[cur_weekday][1], '%H:%M').time())
    print(int((end_of_work_today - dt.combine(cur_dt.date(), cur_time)).seconds / 60), 'минут(а)')
else:
    print('Магазин не работает')




