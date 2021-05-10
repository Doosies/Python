from math import sqrt, floor

def get_num(num):
    result = []
    for i in range(2, floor(sqrt(num))+1 ):
        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 1:
        result.append(int(num))

    return result

num = int(input())
if num > 1:
    for i in get_num(num):
        print(i)
