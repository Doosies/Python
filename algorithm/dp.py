import sys; read = sys.stdin.readline

n = int(read().rstrip())
num = [int(read().rstrip()) for _ in range(n)]

for i in range(len(num), 0, -1):
    for j in range(1, i):
        if num[j] < num[j-1]:
            num[j], num[j-1] = num[j-1], num[j]
print("\n".join(map(str,num)))
