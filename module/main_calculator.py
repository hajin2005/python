from calculator import calculator

# print(calculator.add(1,2))

# print(calculator.div(6,3))

# print(calculator.mul(8,9))

# 숫자 입력 받아서 해보기
num1 = int(input('첫번째 수는? : '))
num2 = int(input('두번째 수는? : '))

print(calculator.add(num1, num2))

print(calculator.div(num1, num2))

print(calculator.mul(num1, num2))