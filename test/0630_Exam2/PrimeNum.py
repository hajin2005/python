#prime_2314 이해하기
#N을 입력받아 1~N까지 소수와 그 개수를 출력하는 프로그램
#하나의 수를 매개변수로 입력받아 소수여부를 판단하는 사용자정의함수
#작성된 함수를 이용하여 결과 출력

print('1~N까지의 소수와 그 갯수를 구하는 프로그램')

num = int(input('N 입력 : '))

def isPrimeNumber(n):
    prime_count = 0

    for i in range(1,n+1):
        count = 0
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            prime_count += 1

    return prime_count       

print(isPrimeNumber(num))