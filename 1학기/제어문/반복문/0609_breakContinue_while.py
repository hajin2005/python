#83p continue
for i in range(1,9+1):
    if i%2 ==0:
        continue
    print('2 x {} = {}'.format(i,2*i))

#83p 리슽츠 컴프리헨션
arr = []
for i in range(9,0,-2):
    arr.append(i*i)
print(arr)

arr = [i*i for i in range(1,10,2) if i*i > 30]
print(arr)

echo = input()
while echo != 'exit':
    print(echo)
    echo = input()

echo = input()
while True:
    if echo == 'exit':
        break
    print(echo)
    echo = input()