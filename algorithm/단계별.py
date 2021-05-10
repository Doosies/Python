from math import sqrt,floor

start = int(input())
end = int(input())
li = []

def is_decimal(num):
    for i in range(2, floor(sqrt(num))+1 ):
        if num % i == 0:
            return False
    return True

for i in range(start, end+1):
    if is_decimal(i) and i > 1:
        li.append(i)

if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))