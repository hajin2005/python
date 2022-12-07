#2개의 문자열을 입력 받아 교집합 문자를 출력
#2개의 문자열의 교집합 문자를 리스트에 저장하여 반환하는 함수
#작성된 함수를 호출하여 결과를 list 오름차순으로 정렬하여 출력
s1 = input('첫 번째 문자열 입력 : ')
s2 = input('두 번째 문자열 입력 : ')

str1 = list(s1)
str2 = list(s2)

def intersect(listA,listB):
    li =[] #교집합 문자 담는 리스트 생성
    result = [] #결과를 반환할 리스트 생성

    for i in listA:
        for j in listB:
            if i==j:
                li += i
    
    #중복 제거를 위해 set으로 변환 후 결과값을 반환할 변수에 저장
    result = list(set(li))
    result.sort() #예쁘게 오름차순으로 정렬

    return result 
    
print(f'교집합 문자 출력 : {intersect(str1, str2)}') #함수 호출