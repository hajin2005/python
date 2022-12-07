#연봉과 근무평가 등급 입력받고 연봉 인상액과 새 연봉을 계산하여 출력
#우수 등급 연봉 6% 인상, 보통 등급 연봉 4%, 불량등급 연봉 2% 인상

money = int(input('현 연봉을 입력하세요 : '))
x = str(input('근무평가등급을 입력하세요 : '))

if x == '우수':
    plus = (money*0.6)
elif x == '보통':
    plus = (money*0.4)
elif x == '불량':
    plus = (money*0.2)
    
money += plus    
print('연봉인상액 : ',plus)
print('새 연봉인상액 : ',money)