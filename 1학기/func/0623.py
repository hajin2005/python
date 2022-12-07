import random

def rolling_dice(pip, repeat):
    for r in range(1, repeat+1):
        n = random.randint(1,pip)
        print(pip, "면 주사위 굴린 결과", r," : ",n)

rolling_dice(4,3)
rolling_dice(10,4)

#데이터 입력하여 합을 구하는 함수 정의
def func_sum(data):
    lst = list(data.split(" "))
    
    sum = 0
    for i in range(len(lst)):
        sum += int(lst[i])
    return sum

data_list = input('데이터 입력 : ')
print('합 : ',func_sum(data_list))
