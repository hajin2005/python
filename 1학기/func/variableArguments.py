#매개 변수에 가변 인수가 있는 함수
#여러 문자열의 합집합 문자를 구하여 다음과 같이 출력되도록 함수 union()작성
#함수 : union(가변인자) , test -> 0630_Exam2 -> intersection 참고

# A -> HAM B -> SPAM  C = []에서는 합집합 문자만 대입

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    
    return result

print(union("HAM","SPAM"))
