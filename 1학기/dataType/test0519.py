#1. 세트 : a 리스트에서 중복된 숫자들을 제거해 보자.
a = [1,1,1,2,2,3,3,3,4,4,5]
b = list(set(a))

print("원본 : ",a)
print("중복제거 후 : ",b) #list(),set() =>리스트와 셋으로 생성하는 함수

#2. a의 첫번째 요소값을 변경하면 b의 값은 어떻게 될까?
a=b=[1,2,3] #얕은 복사
print("a의 주소",hex(id(a)),"\t",'b의 주소',hex(id(b)))
a[1]=4
print(a)
print(b)
print("a의 주소",hex(id(a)),"\t",'b의 주소',hex(id(b))) 
