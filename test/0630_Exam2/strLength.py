#문자열을 입력하여 문자열의 길이만큼 '반짝~'이라는 글자를 출력하는 프로그램 작성
str = input('문자열 입력 : ')

message = "반짝~"
result = message*len(str)
print(result)