import random
from unittest import result

def lotto():
    result = random.sample(range(1,45),6)
    result.sort()
    return result

print(lotto())