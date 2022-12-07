#mutable : 변경되는 객체    immutable : 변경되지 않는 객체, 값이 같으면 주소값이 같다!!!!!!!!!!!!
print("====immutable 객체====")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))
print(hex(id(e)))

print("====mutable 객체====") #값이 자유롭게 바뀔 수 있기 때문에 각각의 메모리를 할당함
arr1 = [1,2,3]
arr2 = [1,2,3]
arr3 = [1,2,3]
arr4 = [1,2,3]
print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
print(hex(id(arr4)))

#imutable 객체 : int 값 변경시
num1 = 99
num2 = 99
print(hex(id(num1)))
print(hex(id(num2)))

num1 += 1
num2 += 3
print('int 값 변경시 ',hex(id(num1))) #주소도 바뀜
print('int 값 변경시 ',hex(id(num2)))

##imutable 객체 : str 값 변경시
print("##imutable 객체 : str 값 변경시")
s1 = "BlockDmask"
s2 = "BlockDmask"
s3 = "BlockDmask"
s4 = "BlockDmask"
print(hex(id(s1)),hex(id(s2)),hex(id(s3)),hex(id(s4)))
s1 = s1.replace('D','zzz')
s4 = s3.upper()
print(hex(id(s1)),hex(id(s2)),hex(id(s3)),hex(id(s4)))

#mutable 객체 : list, set, dictionary, 값이 같아도 주소는 다르지만, 한 객체의 값이 바뀌어도 주소는 계속 같음
arrA = ['a','b',77]     #list 객체
arrB = ['a','b',77]
print(hex(id(arrA)))
print(hex(id(arrB)))
arrA.append(10)
arrB.append(10)
print(hex(id(arrA)))
print(hex(id(arrB)))

print("=====dictionary 값이 변경되면?=====")
d1 = {'a':11, 'b':22}
d2 = {'a':11, 'b':22}
d3 = {'a':11, 'b':22}
print(hex(id(d1)))
print(hex(id(d2)))
print(hex(id(d3)))
d1['a'] = 99
d2['b'] = 39
print(hex(id(d1)))
print(hex(id(d2)))