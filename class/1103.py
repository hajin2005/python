class Person:
    def a_method(self):
        print('a_method가 호출되었습니다.')
    
    def b_method(self):
        self.a_method() #self를 사용하여 호출
        a_method()


def a_method():
    print('클래스 외부에 정의된 a_method')

p1 = Person()
p1.a_method()
p1.b_method()