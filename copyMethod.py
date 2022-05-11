#copy 메서드를 이용한 얕은 복사
arr1 = [4,5,6,[2,4,8]]
arr2 = arr1.copy()  #여기서 복사
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')    #arr1과 arr2의 주소 다름 => [:]과 같음

arr2.append(22) #arr2에 값 추가
print(f'arr1 : {hex(id(arr1))}')
print(f'arr2 : {hex(id(arr2))}')    

#[2,4,8]
print(f'arr1[3] : {hex(id(arr1[3]))}')  
print(f'arr2[3] : {hex(id(arr2[3]))}')  #내부리스트의 주소 같음 
