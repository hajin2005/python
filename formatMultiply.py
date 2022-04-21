x = 2
y = 1

for x in range(2,4):
    print('\n===={0}단===='.format(x))
    for y in range(1,10):
        print("{0} * {1} = {2}".format(x,y,x*y))