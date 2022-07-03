#2개의 문자열을 입력 받아 교집합 문자를 출력
#2개의 문자열의 교집합 문자를 리스트에 저장하여 반환하는 함수
#작성된 함수를 호출하여 결과를 list 오름차순으로 정렬하여 출력
s1 = input('첫 번째 문자열 입력 : ')
s2 = input('두 번째 문자열 입력 : ')

str1 = list(s1)
str2 = list(s2)

def intersect(a, b):
    sum = list(set(a) & set(b))
    sum.sort() #sort()는 list 안에서 값들만 바꿔주지만 그 상태로 반환이 되지 않음.
    return sum

result = intersect(str1, str2) 
#오름차순 정렬 수정
print(type(result))
print(result)
