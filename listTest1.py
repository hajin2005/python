#List : 값의 나열
colors = ["red",'green','blue'] #자료형: list
print("list:", colors)   

#append() : 기존 리스트 끝에 값을 추가
colors.append("blue")
print("append:",colors)

#insert() : 원하는 위치에 값을 추가
colors.insert(1, "pink")
print("insert:",colors)

#index() : 어떤 값이 어디에 있는지 확인, 2번째 인자를 지정하면 지정된 방 번호 이후부터 검색
print("red의 위치 : ",colors.index("red"))  #red의 위치 [0] 출력
colors+=["red"]
print(colors.index("red",1))
colors+="red"   #colors 리스트에 [r] [e] [d] 저장됨
print(colors)

#count() : 현재 해당 값의 개수를 반환
print(colors.count("red"))
#pop() : 값을 뽑아냄, 값을 지정하지 않았다면??=>끝에서부터 하나씩 뽑아냄
print(colors.pop())
print(colors.pop(1))
print(colors)