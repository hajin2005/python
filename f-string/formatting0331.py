#문자열 포매팅: print("%s 왔나요?" % name[i])
# % 서식문자 : % 기호 뒤에 자료형을 가리킴

num = 50
s = 'my age %d' % num
print(s)

# % 기호 문자 출력
names = ['kim','park','lee']
for name in names:  
    print('my name is %s' % name)
# % 기호 정수 출력
money = 10000
s2 = 'give me %d won' % money
print(s2)
# % 기호 실수 출력
d = 3.141592
print('value %f' % d)


#포매팅 해야할 변수 값이 두 개 이상일 때 () 사용
X = 'my name is %s.age: %d' % ('mirim', 100)
print(X)
#출력해야할 값이 점점 많아 질수록
age = 78
money = 20000
name = 'jang'
weight = 53.21
etc = 'abcde'
Y = 'my name is %s, age: %d, weight: %f, money: %d, etc: %s' % (name,age,weight,money,etc)
print(Y)

# % 서식 문자를 이용한 문자열 포매팅은 언뜻 보면 타입을 정해주기 때문에 정확해 보이지만, 타입을 정해야 하기 때문에 불편한 점도 존재
#이를 개선하기 위해서 str.format 형식 등장
#string formatting
month = 1
while month <= 12:
    print(f'2020년 {month}월')
    month += 1
    
#f-string 포매팅: f'문자열 {변수} 문자열' ex)문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣는다.
#f-string 왼쪽 정렬
a = 'left'
result = f'|{a:<10}|'   #오른쪽 정렬은 :>
print(result)
#f-string 가운데 정렬                    
b = 'mid'
result1 = f'|{s2:^10}|'
print(result1)

#f-string 중괄호 출력 방법
result3 = f'my agae {{{num}}}, {{num}}' #첫번째 num은 숫자, 두번째 num은 문자열
print(result3)

#f-string과 딕셔너리
d = {'name': 'Mirim','gender':'female','age':18}
result4 = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result4)
#f-string을 제일 많이 씀
#f-string과 리스트
n = [100,200,300]
print(f'list: {n[0]},{n[1]},{n[2]}')
for v in n:
    print(f'list with for: {v}')

str = "파이선 연습"
print(len(str))
