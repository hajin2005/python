#2314 하진
#문자열을 입력받아 거꾸로 출력하는 프로그램 작성

str = input('영문자 입력 : ')
lst = [i for i in str] #빈 리스트에 문자열 넣기

lst.reverse() #역순으로 정렬
result = "".join(lst) #공백을 인식하여 리스트->문자열
print(f'거꾸로 출력 : {result}')
