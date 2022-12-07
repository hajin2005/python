#학생들의 점수를 입력받고 점수대별로 해당 학생 수만큼 '*' 찍는 프로그램 작성
#학생이 총 몇명인지

score_lst = input('점수 입력: ').split(' ') #한 줄로 입력 받기
score90 = ''
score80 = ''
score70 = ''
score60 = ''
score50 = ''

for i in score_lst: 
    if int(i) >= 90: #i는 현재 타입이 문자열이므로 형변환을 해준다.
        score90 += '*' #문자열 변수에 '*' 문자 추가
    elif int(i) >= 80: 
        score80 += '*'
    elif int(i) >= 70:
        score70 += '*'
    elif int(i) >= 60:
        score60 += '*'
    else:
        score50 += '*'
    
    max_score = max(score_lst) #max 내장함수
    min_score = min(score_lst) #min 내장함수

print('90점 이상   : ',score90)
print('80점 대     : ',score80)
print('70점 대     : ',score70)
print('60점 대     : ',score60)
print('60점 미만   : ',score50)
print('최고점수 : ',max_score)
print('최저점수 : ',min_score)
