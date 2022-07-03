print("mutable 객체 요소로 존재하는 immutable, mutable")

#arr1과 arr2가 가리ㅣ키는 리스트의 주소는 분명 다를 것이다. (mutable이니까)
#mutable 객체 안에 있는 immutable
arr1 = [55,66,[11,22],'a','b']
arr2 = [55,66,[11,22],'a','b']
print(f'')

#리스트(immutable) 객체의 주소
#그 안에 있는 immutable 인 55,66,'a','b'는 어떨까
print({hex(id(arr1[0]))})
print({hex(id(arr2[0]))})
print({hex(id(arr1[1]))})
print({hex(id(arr2[1]))})
print({hex(id(arr1[3]))})
print({hex(id(arr2[3]))})
print({hex(id(arr1[4]))})
print({hex(id(arr2[4]))})
#그 안에 있는 mutable 인 list는 어떨까?
print("리스트 내부의 mutable 요소들")
print({hex(id(arr1[2]))})
print({hex(id(arr2[2]))})

#얇은 복사 : 주소가 복사되어 객체를 공유하는 얕은 복사
print("얇은 복사 : 주소가 복사되어 객체를 공유하는 얕은 복사")
arr1 = [1,2,3]
arr2 = arr1
arr1.append(4)
print({hex(id(arr1[2]))})   #arr1와 arr2의 주소값이 같다
print({hex(id(arr2[2]))})

print("[:]을 이용한 얕은 복사")
arr1 = [4,5,6,[2,4,8]]
arr2 = arr1[:]  #여기서 복사
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')

arr2.append(22) #arr2에 값 추가
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')

print("\n3.리스트 내부 리스트")
print(f'arr1[3] : {hex(id(arr1[3]))}')
print(f'arr2[3] : {hex(id(arr2[3]))}')

arr1[3].append(99)
print("\n4.리스트 내부 리스트에 값 추가")
print(f'arr1[3] : {hex(id(arr1[3]))}')  #arr1[3]과 arr2[3]부분 바로 저 [2,4,8]
print(f'arr2[3] : {hex(id(arr2[3]))}')  #두 내부 리스트가 동일한 곳을 가리키고 있는 것을 볼 수 있ㄷ.

print("\n5.리스트 내부 리스트")
print(f'arr1 :{arr1} => {hex(id(arr1))}')
print(f'arr2 :{arr2} => {hex(id(arr2))}')
