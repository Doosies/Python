from math import sqrt,floor
n = int(input())
li = map(int, input().split())
cnt = 0

for i in li:
    if i == 1:
        cnt += 1
    else:
        for j in range(2, floor(sqrt(i))+1):
            if i % j == 0:
                cnt += 1
                break
print(n-cnt)
