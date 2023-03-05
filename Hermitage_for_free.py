from datetime import date
import calendar

print('Third Thursday of every month is free in Hermitage!\n')
year = int(input('Please, write year to see the shedule for free visit: '))

def get_days_in_month(year, month):
    last_day_in_month = calendar.monthrange(year, month)[1] + 1
    lst_dates = []
    counter = 1
    for i in range(1, last_day_in_month):
        if int(date(year, month, i).strftime('%w')) == 4:
            if counter == 3:
                lst_dates.append(date(year, month, i))
                break
            else:
                counter += 1
        
    return lst_dates


def get_all_thursdays(year):
    answer = []
    for month in range(1, 13):
        answer += get_days_in_month(int(year), month)
    
    return answer

for th in get_all_thursdays(year):
    print(th.strftime('%d.%m.%Y'))

