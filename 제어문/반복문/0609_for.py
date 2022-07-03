lst = ["apple",100,3.14]
for item in lst:
    print(item, type(item)) #str, int, float

d = {"apple":100, "orange":200, "banana":300}
for key, value in d.items():
    print(key,value, type(key)) 

a = [(1,2),(3,4),(5,6)] #3 7 11이 나오도록 하기
for (x,y) in a:
    print('first:',x,'last:',y)
    print(x+y)

for x in range(1,11):
    print('*'*x) #x=1... x=2... x=3
# for i in range(1,10+1):
#     for j in range(1, i+1):
#         print('*',end='')
#     print()

#구구단
for dan in range(2,5+1):
    for j in range(1,9+1):
        print('{}*{}={}'.format(dan,j,dan*j))
    print()

#별찍기
for i in range(1,6):
    print(' '*(5-i),'*'*(2*i-1))
    print()

#82p
table = [['월','화','수'],[100,200,300]]
for row in table:
    for col in row:
        print(str(col)+' ')
    print()