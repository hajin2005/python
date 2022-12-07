# 카드 게임을 할 수 있도록 도와주는 카드 클래스 정의
# 멤버 변수 : 숫자 변수(1~13까지의 숫자를 저장), 문양변수(문자열 heart, diamond, club, spade)
# 범위에 포함되지 않는 숫자나 정의되지 않은 문양 값 입력시 print() 함수를 사용하여 경고문 출력

class CardGame:
    def __init__(self, num, pattern):
        if(0<num<14):
            self.num = num
        else:
            print('범위에 포함되지 않는 숫자입니다.')

        if(pattern == "heart" or pattern == "diamond" or pattern == "club" or pattern == "spade"):
            self.pattern = pattern
        
        else:
            print('정의되지 않은 문양 값입니다.')