class Person:
    pass

class Monster:
    pass

# 클래스 사용
p1 = Person()
result = isinstance(p1, Person)
print('[1] p1 인스턴스는 Person ㅋㄹ래스의 인스턴스 객체가 맞나요 ->', result)
print('[1] p1 인스턴스는 Person 클래스의 인스턴스 객체가 맞나요 ->', isinstance(p1, Person))
