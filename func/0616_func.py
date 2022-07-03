def times (a,b):
    return a*b

mytimes = times
print(mytimes)  #times 함수의 주소값이 찍힘
print(times) #함수의 주소값이 찍힘
print(mytimes(3,5)) #times 함수가 호출이 되면서 15라는 결과가 나옴
# => 함수도 copy가 가능함!!

#10진수->2진수 변환
print(128, "의 2진수 : ",bin(128))
#10진수 ->16진수 변환
print('16의 16진수',hex(16))
pi = 3.56789
print(round(pi,4)) #n.012345.......

say = '안녕 내 이름은 {0}이고 나이는 {1}이야, 지금도  {2}이고'
print(say.format('하진',18,20))
print((int)(2.888))
print(float(3.0))

list = ['d','c','a','b']
for index, value in enumerate(list): #tuple 형태로 반환하늕....
    print(index, value)

str = '나는 문자열'
print(str)
n=3
print((n)) #오류 발생

import random
n = random.randint(1,6)
print(n)
n = random.randint(1,6)
print(n)
n = random.randint(1,6)
print(n)

def rolling_dice():
    n = random.randint(1,6)
    print(n)

rolling_dice()