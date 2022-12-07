# 2314 하진
# 그룹별로 데이터를 5개씩 입력받아 두 그룹을 병합하여 중복없이 처리하여 오름차순 정렬, 출력

# print('첫번째 그룹의 데이타 : ', end='')

# group_list = [1,2,3,4,5]
group1 = str(input('첫번째 그룹의 데이타 : '))
group2 = str(input('두번째 그룹의 데이타 : '))
    
group1 = group1.split(' ')
group1_list = [0,0,0,0,0]
group2 = group2.split(' ')
group2_list = [0,0,0,0,0]

answer = group1+group2
answer.sort()

print('병합된 그룹의 데이타 : ', end='')
for i in range(len(answer)):
    print(f'{answer[i]} ', end='')