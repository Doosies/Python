import sys; read = sys.stdin.readline

n = int(read().rstrip())
num = [int(read().rstrip()) for _ in range(n)]

for i in range(1, len(num)):
    for j in range(i, 0, -1):
        if num[j-1] > num[j]:
            num[j-1], num[j] = num[j], num[j-1]
print(num)