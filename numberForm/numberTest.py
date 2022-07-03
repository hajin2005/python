print('############################################')

age = 18
print(type(age))

pi = 3.14
print(type(pi))

age /= 2
print(type(age))   #9.0

x = 10 + 3.14   #13.14
print(type(x))

print('===========================================')
print(0b1100111000)
print(0o130)
print(0xD7A)

print(10e3)
print(type(10e3))

print(1.2345E2)
print(type(1.2345E2))
print(1.23456e-2)
print(type(1.23456e-2))
print('===========================================')
print(8+24j)
c = 1.2+3.4J
print(type(1.2+3.4j))
print(c.real) #실수 부분
print(c.imag) #허수 부분
print(c.conjugate())   #켤레 복소수를 구하는 함수
d=1j
print(d.conjugate()) #1j
print(d*d.conjugate())

