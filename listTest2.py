from re import T
from turtle import color

colors = ["red",'green','blue']

#remove() : 단순히 해당 값을 삭제 
print(colors.remove("blue"))    #None
print(colors)
#remove와 pop의 차이?? => 뽑아낸 값을 다시 리턴하고 싶을 땐 pop, 삭제만 하고 싶은 경우는 remove

#extend() : 데이터 추가
colors.extend(["blue","yellow","white"])
print(colors)

#sort() : 오름차순 정렬
colors.sort()
print(colors)
#reverse() : 내림차순 정렬
colors.reverse()
print(colors)

#tuple : 순서가 존재하는 값의 나열, 일반적인 경우에 데이터를 묶어서 한번에 전달하거나 여러 개의 값을 묶어서 한번에 반환할 경우에 사용됨
t = (1,2,3)
print(type(t))
#tuple이 주로 사용되는 경우 : 함수에서 하나 이상의 값을 리턴하는 경우 
def calc(a, b):     #tuple : () 사용 
    return a+b, a*b
x,y = calc(5,4)
print(x,y)
#문자열 포맷팅
print("id : %s, name : %s" % ("kim","김유진"))
#tuple에 있는 값을 함수 인수로 사용하는 경우
args = (3,4)
print(calc(*args))  #(7,12)