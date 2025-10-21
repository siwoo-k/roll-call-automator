import pandas as pd
import read

ranks = {'이병': 0, '일병': 1, '상병': 2, '병장': 3, '선임병장': 4}

work = []
working = {}

file_path = 'OCT.xlsx'

df = pd.read_excel(file_path)

length = int(input('how many work days: '))
day = int(input('enter current day: '))
job = input('enter current job: ')

for j in range(length):
    for i in range(len(df[day])):
        if df[day][i] == job or df[day][i] == 'OJ' + job:
            rank, order, name = read.extract(df['DAYS'][i])
            if df[day][i] == 'OJ' + job:
                name += ' (OJT)'
            work.append((rank, order, name))
            
    work.sort(key=lambda i : (-ranks[i[0]], i[1], i[2]))

    text = ''
    if work[0][1] == work[1][1]:
        lead = work[0][0] + ' OOO'
    else:
        lead = work[0][0] + ' ' + work[0][2]
    for i in work:
        text += i[0] + ' ' + i[2] + '\n'
        
    format = f'단결! {lead} 평택 패트롤 데이 출근 보고드립니다.\n근무자:\n' + text + f'총기 및 탄 드로우 이상 없습니다.\n근무자 건강특이사항: 이상 없습니다.\n단결!\n\n단결! {lead} 평택 패트롤 데이 퇴근 보고드립니다.\n근무자:\n' + text + '총기 및 탄 반납 이상 없습니다.\n근무자 건강특이사항: 이상 없습니다.\n단결!'
    
    print(f'{day}OCT25')
    print(format)
    print()
    format = ''
    work = []
    day += 1