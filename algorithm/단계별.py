import sys
read = sys.stdin.readline

n = int(read().rstrip())
count_list = [0 for _ in range(10001)]

for i in range(n):
    count_list[int(read().rstrip())] += 1
    
for i in range(1, 10001):
    for j in range(count_list[i]):
        print(i)