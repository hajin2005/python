#1. 홍길동씨의 주민번호 881120-1068234 , 주민등록번호를 연월일과 뒤의 숫자 부분으로 나누어 출력하자
num = "881120-1068234"
print("성별 : "+num[7])

#2. 리스트 [1,3,5,4,2] => [5,4,3,2,1]
list = [1,3,5,4,2]
list.sort()
list.reverse()
print(list)

#3. ['Life','is','too','short'] 쭈욱 출력
list2 = ['Life','is','too','short']
print(" ".join(list2))  #리스트를 " "로 이어서 문자열 만들기

#4. 튜플 (1,2,3)에 4fksms rkqt cnrk 
tuple = ()
tu1 = (1,2,3)
tu2 = (4,)
tuple = tu1+tu2
print(tuple)

#5. 딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제
a = {'A':90,'B':80,'C':70}
print("원본 : ",a)
b = a.pop('B')
print("'B'추출 후 딕셔너리 : ",a)
print("추출된 B의 값 : ",b)