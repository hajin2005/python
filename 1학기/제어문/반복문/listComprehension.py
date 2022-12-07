print(list(range(10)))
print(list(range(10,20,2)))
print(list(range(5,10)))
print(list(range(10,0,-1)))

#리스트 함축 comprehension
#기존의 리스트 객체를 이용해 조합, 필터링 등의 
#추가적인 연산을 통해 새로운 리스트 객체를 생성하는 경우 '리스트 내장'이 매우 효율적
lst = [1,2,3,4]
print(lst)
lst = [i**2 for i in lst] #for:1~4까지 => i=1의 제곱 => 1 => i=2 => 2의 거듭제곱
print(lst)

d = {100:'apple',200:'banana',300:'orange'}
d_upper = [v.upper() for v in d.values()] #객체.upper(): 문자열의 객체를 대문자로 변경
print(d_upper)

#반복문 작성 시 도움이 되는 함수: filer(func or None, 자료형 객체)
lst = [10,25,30]
iteL = filter(None, lst) #필터링을 적용할 수 있는 함수, 순회가능한 객체
for item in iteL:
    print('item:{0}'.format(item))

def getBiggerThan20(i):
    return i>20
print()
iteL = filter(getBiggerThan20, lst)
for item in iteL:
    print('item:{0}'.format(item))