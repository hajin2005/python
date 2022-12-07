# -13 -10 5 8
# minus plus
#odd even odd even
a = int(input("숫자 입력 : "))

if a<0: #음수
    print('minus')
    if a%2==0:
        print('even')
    else:
        print('odd')

elif a>0: #양수
    print('plus')
    if a%2==0:
        print('even')   #짝수
    else:
        print('odd')    #홀수