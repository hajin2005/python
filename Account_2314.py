# 2314 하진
# 메뉴 1.
import random

#1. 계좌생성
def createAccount(): 
    num = random.randint(0,999999999)
    return num

# 2. 입금
def deposit(account, my_money):
    while True:
        a = int(input('계좌번호 입력 : '))
        if(account != a):
            a = int(input('계좌번호 입력 : '))

        else:
            money = int(input('입금 금액 : '))
            my_money += money
            break

    return my_money

# 3. 출금
def withdraw(account ,my_money):
    while True:
            a = int(input('계좌번호 입력 : '))
            if(account != a):
                a = int(input('계좌번호 입력 : '))

            else:
                money = int(input('출금 금액 : '))
                if(my_money >= money):
                    my_money -= money
                    break
                else:
                    print('잔액이 출금액보다 적습니다.')
                    break
    return my_money
    


# 계좌번호 체크 함수
# def checkAccount(bank):
#     while True:
#         account = int(input('계좌번호 입력 : '))
#         for key in bank.keys():
#             if(account != key):
#                 account = int(input('계좌번호 입력 : '))
#             else:
#                 # 해당 계좌의 잔액 리턴
#                 answer = bank.get(account)
#                 break
    
#         return answer

    
        
while True:
    print('====================================================')
    print('계좌관리')
    print('====================================================')
    print('1. 계좌생성  2. 입금 3. 출금 4. 잔액조회     0. 종료')
    print('====================================================')
    menu = int(input('메뉴 선택 : '))
    bank = {}

    if(menu == 1):
        new_account = createAccount()
        # bank[new_account] = 0 #키 : 새로 만든 계좌, 값 : 잔액(0)
        my_money = 0
        print(f'계좌번호 {new_account}인 계좌가 생성되었습니다.')

    elif(menu == 2):
        my_money = deposit(new_account, my_money) #계좌번호와 잔액이 들어있는 딕셔너리 전달
        print(f'현재 잔액은 {my_money}원 입니다.')
    elif(menu == 3):
        my_money = withdraw(new_account,my_money)
        print(f'현재 잔액은 {my_money}원 입니다.')

    elif(menu == 4):
        print('====================================================')
        print('계좌번호         잔액')
        print('====================================================')
        print(new_account, my_money)
        
    elif(menu == 0):
        print('프로그램을 종료합니다.')
        break
    
    else:
        print('존재하지 않는 메뉴입니다.')