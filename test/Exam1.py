#2314 하진

#1. 두 개의 정수를 입력받아 구구단 출력
x = int(input('정수1 입력: '))
y = int(input('정수2 입력: '))

print()
for dan in range(x,y+1):
    print('{}단'.format(dan))
    for i in range(1,9+1):
        print('{} * {} = {}'.format(dan,i,dan*i))
    print()

#2. 5개의 정수를 입력하여 합과 평균(소수 두 자리까지 출력, 평균 60이상이면 합격 or not 불합격)
a = int(input('정수1 입력: '))
b = int(input('정수2 입력: '))
c = int(input('정수3 입력: '))
d = int(input('정수4 입력: '))
e = int(input('정수5 입력: '))

sum = a+b+c+d+e #합계 계산
average = sum/5.0   #평균 계산
average = "{:1.2f}".format(average) #소수점 둘째자리까지 

#출력
print('입력된 점수 : ',a,b,c,d,e)
print('합계 : ',sum)
print('평균 :',average)
#조건 검사
if float(average) >= 60:
    print(average,'점으로 합격입니다.')
else:
    print(average,'점으로 불합격입니다.')

#3.딕셔너리 상품명 key, 가격과 수량 value로 데이터 처리
#[key][0] : 가격, ['상품명'][1] : 수량
price_quantity = {"메로나":[1000,20],"비비빅":[700,3],"바밤바":[850,100]}

#3-6
w = 3
while w < 6:
    print()
    print('1. 신규 상품 등록')
    print('2. 상품 수정')
    print('3. 상품 삭제')
    print('4. 상품 조회')
    print('0. 종료')
    m = int(input('메뉴 입력 : '))
    if m == 1:
        #3-2. 신규 상품 등록
        print('1. 신규 상품 등록')
        newKey = str(input('상품명 입력 : '))
        newPrice = int(input('가격 입력 : '))
        newQuantity = int(input('수량 입력 : '))
        price_quantity[newKey] = [newPrice][newQuantity]

        #06/02 수정해야할 부분 : 3-1왼쪽, 오른쪽 정렬(왼쪽정렬{범위1:<범위2})
        print('상품명\t가격\t수량') #상품조회
        for key in price_quantity.keys():
            print(key,'\t',price_quantity[key][0],'\t',price_quantity[key][1]) #상품명   가격   수량
    elif m==2:
        #3-3. 상품 수정 작성
        print('2. 상품 수정')
        name = str(input('상품명 입력 : '))
        #가격, 수량 선택
        print('1. 가격 수정')
        print('2. 수량 수정')
        fix = int(input('메뉴 입력 : '))
        if fix == 1:
            #가격 수정
            fixPrice = int(input('가격 입력 : '))
            price_quantity[name][0] = fixPrice
        elif fix == 2:
            #수량 수정
            fixQuantity = int(input('수량 입력 : '))
            price_quantity[name][1] = fixQuantity

        print('상품명\t가격\t수량') #상품 조회
        for key in price_quantity.keys():
            print(key,'\t',price_quantity[key][0],'\t',price_quantity[key][1])   

    elif m==3:
        #3-4  원하는 상품 삭제
        print('3. 상품 삭제')
        #상품 삭제
        name2 = str(input('상품명 입력 : '))
        del price_quantity[name2]

        print('상품명\t가격\t수량')
        for key in price_quantity.keys():
            print(key,'\t',price_quantity[key][0],'\t',price_quantity[key][1])
        print()

    elif m==4:
        #3-1. 상품 조회
        print('4. 상품 조회')
        print('상품명\t가격\t수량')
        for key in price_quantity.keys():
            print(key,'\t',price_quantity[key][0],'\t',price_quantity[key][1])
        print()
    
    elif m==0:
        #3-5 실행을 종료하는 프로그램
        print()
        print('프로그램을 종료합니다.')
        break