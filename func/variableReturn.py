#리스트를 사용해 여러 값을 하나로 리턴하는 함수

def multi_num(multi, start, end):
    result = []

    for n in range(start, end):
        if n % multi == 0:
            result.append(n)
    
    return result

multi2 = multi_num(17,1,200) #1~200까지 17의 배수 찾는 함수 
print('multi_num(17,1,200) : ',multi2)

def min_max(*args):
    min = args[0]
    max = args[0]

    for arg in args:
        if min > arg:
            min = arg
        
        if max < arg:
            max = arg
    
    return min, max

print('')

#이름을 입력받아 성과 이름을 나누어 리턴하는 함수 div_name

def div_name(name):
    name

result = div_name('ha jin')
print('div_name('hajin') = ',result)