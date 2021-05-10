from math import sqrt, floor

a, b = map(int, input().split())
li = []
def is_decimal(num):
    for i in range(2, floor(sqrt(num))+1 ):
        if num % i == 0:
            return False
    return True

for i in range(a,b+1):
    if is_decimal(i) and i > 1:
        li.append(i)

for v in li:
    print(v)         