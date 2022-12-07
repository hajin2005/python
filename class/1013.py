class Car:
    def __init__(self, type, speed): #생성자메서드
        self.type = type 
        self.speed = speed
        print(self.type)
        print('객체 생성')

    def move(self):
        print(self.type,'의 속도 : ',self.speed)

    def speed_up(self, amount):
        self.speed += amount
    
    def speed_down(self, amount):
        self.speed -= amount        

c = Car("스포츠카",100)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()