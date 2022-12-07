#1. 입력받은 양의 정수 3,5,8의 배수인지 알려주는 프로그램 작성
num = int(input('수 입력: '))
if num % 3==0:
    print('{}은(는) 3의 배수이다.'.format(num))
if num % 5 == 0:
    print('{}은(는) 5의 배수이다.'.format(num))
if num % 8 == 0:
    print('{}은(는) 8의 배수이다.'.format(num))
if num%3 != 0 and num%5 !=0 and num%8 != 0:
    print('어느 배수도 아니다')
