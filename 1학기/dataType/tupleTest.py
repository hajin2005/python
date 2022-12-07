#튜플
t = ()
xy = (2560, 1440)
color = 129,247,216
print(xy)
print(color)
print(xy+color)

color = 129,247,216 #패킹
print(color)
red, green, blue = color #언패킹 (약간 해제하는 ...느낌)
print(color)
print(red) #129

a = (123,"abc",True,123)
print(a[:2])    #a[0]~a[1] =>123, 'abc'

print(a.count(123)) #2

#test
t = (1,2,3)
print(t)
t+= (4,)
print(t)