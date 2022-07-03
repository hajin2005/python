import copy
#1. copy 메서드를 이용한 얕은 복사
arr1 = [4,5,6,[2,4,8]]
arr2 = arr1.copy()  #여기서 복사
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')    #arr1과 arr2의 주소 다름 => [:]과 같음

#리스트 내부에 있는 리스트 주소 비교
print('리스트 내부에 있는 리스트 주소 비교') #주소 같음
print(f'arr1 in list {arr1[3]} : {hex(id(arr1[3]))}')
print(f'arr2 in list {arr2[3]} : {hex(id(arr2[3]))}')

arr2.append(22) #arr2에 값 추가
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')    

#[2,4,8]
print(f'arr1[3] : {hex(id(arr1[3]))}')  
print(f'arr2[3] : {hex(id(arr2[3]))}')  #내부리스트의 주소 같음 
print("=================================================")

#2. copy 모듈의 copy 함수 : copy 메서드와의 차이점은 매개변수가 필요함
arr1 = [4,5,6,[2,4,8]]
arr2 = copy.copy(arr1)  #여기서 복사
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}') 

arr2.append(22) #arr2에 값 추가
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')  
#[2,4,8]
print(f'arr1[3] : {hex(id(arr1[3]))}')  
print(f'arr2[3] : {hex(id(arr2[3]))}')  #내부리스트의 주소 같음

print("=================================================")
print("copy모듈의 copy 함수를 이용한 얕은 복사 DICTIONARY")
d1 = {'a':'Mirim','b':[1,2,3]}
d2 = copy.copy(d1)
print(f'd1 : {hex(id(d1))}')
print(f'd2 : {hex(id(d2))}') #주소값이 다름

d2['c'] = 'kim'
print(f'd1 : {hex(id(d1))}')
print(f'd2 : {hex(id(d2))}')
print("dictionary 내부에 리스트 value")
print(f"d1 : {hex(id(d1['b']))}")
print(f"d2 : {hex(id(d2['b']))}")   #주소값 동일 