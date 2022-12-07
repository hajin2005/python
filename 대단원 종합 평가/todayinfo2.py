# datetime 클래스를 이용하여 오늘 날짜와 현재 시각 구하고 
# weekday 메소드를 이용하여 오늘 날짜, 요일 정보 출력

from datetime import *

today_date = date.today() # 오늘 날짜 구하기
current_time = datetime.now() #현재 시각 구하기

def weekday(date, weekday):
    
    date = str(date).split('-')

    if(weekday==0): weekday = '월요일'
    elif(weekday==1): weekday = '화요일'
    elif(weekday==2): weekday = '수요일'
    elif(weekday==3): weekday = '목요일'
    elif(weekday==4): weekday = '금요일'
    elif(weekday==5): weekday = '토요일'
    else: weekday = '일요일'

    answer = f'오늘은 {date[0]}년 {date[1]}월 {date[2]}일 {weekday}입니다.'

    return answer

print(weekday(today_date, today_date.weekday()))
# 요일 정보 : date.today().weekday()