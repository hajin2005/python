# 이건 시험공부해라 !!!!!!!!!!!!!!!!!!!!!!
class Car:
    count = 0
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    @classmethod
    def get_count(cls): #self 매개변수 필요하지 않음, 
        return Car.count #count 값을 넣을 객체 생성을 하지 않아도 됨

# @classmethod - cls 를 사용했을 경우 객체 생성을 먼저 하지 않아도 됨.
# print(Car.get_count()) -> 매개변수 self로 작성했을 경우 에러, 객체 생성 후 사용해야함

c1 = Car("스포츠카",100)
c2 = Car("트럭",50)
print(Car.get_count())