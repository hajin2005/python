from calculator import calculator
n1 = int(input('n1 입력 :'))
n2 = int(input('n2 입력 :'))

print(calculator.add(n1, n2))
print(calculator.sub(n1, n2))
print('n1(4) * n2(8) = ',calculator.mul(n1=4, n2=8))