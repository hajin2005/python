#입력 받은 수가 소수인지 판별하는 프로그램을 작성하라
#n이 소수인지 판별하기 위해서는 2부터 n까지의 숫자 중 나누어서 0인 숫자있고
#그 숫자가 n과 다르다면 소수가 아니다.
#나누어떨어진 숫자가 n과 같다면 그 수는 소수이다.
num = int(input('수 입력: '))

def primeNum(n):
    for i in range(2, n):
        if n%i==0 :
            return False
    return True

result = primeNum(num)
if result == True:
    print('소수이다.')
else:
    print('소수가 아니다.')