phone = {"kim":"1111","lee":"2222","park":"3333"}
print(phone.keys())
print(phone.values())

print("park" in phone)  #true
print("moon" in phone)  #false

#for문으로 참조하기
d = {"a":100, "b":200, "c": 300}
for key in d.keys():
    print(key)

for value in d.values():
    print(value)