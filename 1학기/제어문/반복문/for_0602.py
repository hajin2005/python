for x in range(3,9,2):
    print(x)

for ch in "LOVE":
    print(ch)

for item in {"HTML5","CSS3","JavaScript"}:
    print(item)

table = [["월","화","수"],[100,200,300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

lst = ['apple',100,3.14]
for value in lst:
    print(value, type(value))