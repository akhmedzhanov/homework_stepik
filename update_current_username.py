'''
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты,
в третьем — дата и время изменения. При этом email пользователь менять не может, только имя.
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя
и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов
такие же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке
названий электронных ящиков пользователей.
'''


import csv
from datetime import datetime

with open('name_log.csv', 'r', encoding='utf-8') as file:
    
    users = csv.DictReader(file)
    columns = users.fieldnames #username,email,dtime

    info = sorted([[user['username'], user['email'], datetime.strptime(user['dtime'], '%d/%m/%Y %H:%M')] for user in users], key=lambda x: x[2])
    answer = {i[1]: [i[0], i[2]] for i in info}

    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(columns)
        for a, value in sorted(answer.items()):
            writer.writerow([value[0], a, value[1].strftime('%d/%m/%Y %H:%M')]) #datetime format: 17/11/2021 01:17
