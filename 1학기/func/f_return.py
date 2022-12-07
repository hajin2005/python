#return 값이 없는 경우
from this import s


def setValue(newValue):
    x = newValue

retValue = setValue(10)
print(retValue) #None

#return 값이 있는 경우
def swap(x, y):
    return x,y

print(swap(1,2))

#하나의 값을 리턴하는 함수
def sum(*num):
    s =0
    for item in num:
        s += item
    return s

result = sum(1,3)
print("1 + 3 = ",result)

print('매개변수 중 가장 작은 값 하나만 리턴하는 함수 작성')
def min(*num):
    min = num[0]
    for item in num:
        if item < min:
            min = item
    
    return min

result = min(1,2)
print('min(1,2) = ',result)