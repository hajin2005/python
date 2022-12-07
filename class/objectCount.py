class Person:
    #클래스 변수
    count_class_var = 0

    # 생성자
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        self.increase_obj()

    # @classmethod
    def increase_obj(self):
        Person.count_class_var += 1
        print(Person.count_class_var)
    
print('현재까지 생성된 인스턴스 객체의 갯수')
p1 = Person('김홍철', 30, 'pwr')
print('현재까지 생성된 인스턴스 객체의 갯수')
p2 = Person('유재석', 40, 'pwr2')
print('현재까지 생성된 인스턴스 객체의 갯수')
p3 = Person('정준하', 50, 'pwr3')
