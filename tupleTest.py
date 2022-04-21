#튜플
t = ()
xy = (2560, 1440)
color = 129,247,216
print(xy)
print(color)
print(xy+color)

#패킹
color = 129,247,216
print(color)
red, green, blue = color
print(color)
print(red)

a = (123,"abc",True,123)
print(a[:2])    #a[0]~a[1]

print(a.count(123))

#test
t = (1,2,3)
print(t)
t+= (4,)
print(t)