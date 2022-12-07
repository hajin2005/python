# 인자 전달 : 불변형식을 사요할 경우 지역 영역에서 전역 영역의 변수를 사용하고 싶을 때

g = 1

def testScope(a):
    global g #함수밖에 있는 변수 부르기
    g = 2
    return g+a

print(testScope(1))  # 3
print(g)  # 2
