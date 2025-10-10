import pandas as pd
import read

ranks = {'이병': 0, '일병': 1, '상병': 2, '병장': 3, '선임병장 상병': 4, '선임병장 병장': 5}

work = []
working = {}

file_path = 'OCT.xlsx'

df = pd.read_excel(file_path)

day = int(input('enter current day: '))
job = input('enter current job: ')

for i in range(len(df[day])):
    if df[day][i] == job or df[day][i] == 'OJ' + job:
        work.append(read.extract(df['DAYS'][i]))
        
work.sort(key=lambda i : (-ranks[i[0]], i[1]))
for i in work:
    print(i[0] + ' ' + i[1])