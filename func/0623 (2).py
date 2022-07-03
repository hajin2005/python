#가변인자!!!!!!!!!

def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + " " + (space*space_num) + " " + args[i] + " "
    print(str)

p(",",3,"♡","♪")
p("♠",2,"♡","♪","♣")

print('혼자 해보기!!\n')
#star 함수 정의
def star(shape,*n):
    for i in range(0, len(n)):
        print(shape*n[i])
    
star("♪",3)
star("♠",1,2,3)

def fn(a,b,c,d,e):
    print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(a=1,b=2,c=3,d=4,e=5)