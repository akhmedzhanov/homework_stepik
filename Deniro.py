'''
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу.
Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа,
и в лексикографическом порядке слов, если столбец содержит слова.
'''

import csv

with open('deniro.csv', 'r', encoding='utf-8') as file:
    sorting_col = int(input()) - 1
    data = [r.split(',') for r in  file.read().splitlines()]
    for r in sorted(data, key=lambda x: int(x[sorting_col]) if x[sorting_col].isdigit() else x[sorting_col]):
        print(*r, sep=', ')
