from datetime import date, datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() : ',today)
print("연, 월, 일 : ", today.year, today.month, today.day)
print('시, 분, 초:', today.hour, today.minute, today.second)
print('요일 : ', today.weekday())
print('특정 날짜 시각 객체 만들기')
day = datetime(2018, 1,1,0,0,0)
print(day)
print('2018년부터 지나온 시간 구하기')
print(today-day)

print('=============================test====================================')
christmas = datetime(2022, 12,25,0,0,0)
print('크리스마스까지 남은 날짜는?')
today = datetime.now()
print((christmas - today).days)