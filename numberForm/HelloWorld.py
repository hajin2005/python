import math
print(331/17) #나누기는 무조건 float형
x = 37
y = math.pow(x,2)   #float형
print(y)
y = math.pow(10,10) #float형
print(y)

y = 123+456j
print(y.conjugate()) #y의 켤레복소수

fun = "funny day"
print(fun[-6:9])

print(fun.replace("day","Life"))
mon = [31,28,31,30,31,30,31,31,30,31,30,31]

h = 3
m = 15
h,m = m,h #값 변경
print(h,m)