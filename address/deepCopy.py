import copy
#깊은 복사는 내부에 있는 객체 모두 새롭게 만들어주는 작업
print("==================================")
arr1 = [1,2,[99,88,77],3]
arr2 = copy.deepcopy(arr1)
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')    

print('======내부에 있는 객체 주소 비교=======') #주소 다름
print(f'arr1 in lst : {hex(id(arr1))}')
print(f'arr2 in lst : {hex(id(arr2))}')

print("==================================")
print("리스트에 새 key, value 추가")
arr1.append(0)
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')

print("==================================")
print('리스트 내부 리스트')
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')

print("==================================")
print('리스트 내부 리스트에 값 추가')
arr1[2].append(9)
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')
#arr1과 arr2의 주소값 다름, 리스트의 내부 리스트의 주소값도 각각 다름 => 깊은 복사!!