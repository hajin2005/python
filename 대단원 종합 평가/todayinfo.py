from calendar import week, weekday
from datetime import datetime
from unittest import result

today = datetime.today()
weekday = today.weekday()
week =''

if weekday == 0:
    week = '월'
elif weekday == 1:
    week = '화'
elif weekday == 2:
    week = '수'
elif weekday == 3:
    week = '목'
elif weekday == 4:
    week = '금'
elif weekday == 5:
    week = '토'
else:
    week = '일'

result_format = "오늘은 {:d}년 {:d}월 {:d}일 {}요일"
result = result_format(today.year, today.month, today.day, week)
print(result)