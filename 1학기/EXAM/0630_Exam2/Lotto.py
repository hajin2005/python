#lotto 당첨 번호를 예측하는 프로그램을 작성하고자함. 
#1~45까지의 수 중 6개 중복없이 임의로 발생시켜 저장하는 사용자 정의 함수 작성
#작성된 함수를 10번 호출하여 10번의 결과를 오름차순 정렬하여 출력

import random #난수 생성하기 위해서 random 임포트

def func_lotto(): #당첨 번호 뽑기 
    list = []
    for i in range(6):
        randomNum = random.randint(1,45)
        
        if randomNum in list:
            randomNum = random.randint(1,45)
        list.append(randomNum) #리스트에 6개의 숫자 append하기
    
    lst = [str(i) for i in list]
    
    return ' '.join(lst) #, 기호 없애기

#주의! func_lotto : 함수를 호출할 때 괄호가 없으면 주소값이 찍힘
for i in range(1,11):
    print('당첨된 번호 : ',func_lotto())
