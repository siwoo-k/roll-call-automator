import pandas as pd
work = []
working = {}

file_path = 'OCT.xlsx'

df = pd.read_excel(file_path)

day = int(input('enter current day: '))
job = input('enter current job: ')

for i in range(len(df[day])):
    if df[day][i] == job or df[day][i] == 'OJ' + job:
        work.append(df['DAYS'][i])
    
