import random

print('0이상 1미만 실수 값')
print('random.random()=',random.random())
print()

print('시작값 2.5이상 끝값 10.0 미만 실수 값')
print('random.uniform(2.5, 10.0)=',random.uniform(2.5,10.0))
print()

print('1 이상 끝값 7미만, 증가 값이 2인 정수 값')
print('random.randrange(1,7,2)=', random.randrange(1,7,2))
print()

print('리스트에서 1개 값 꺼내오기')
season = ['봄','여름','가을','겨울']
print('season = ',season)
print('random.choice(season) : ',random.choice(season))

# 리스트에서 몇 개의 값을 중복하지 않고 3개 뽑기
# random.sample