import sys; read = sys.stdin.readline

n = int(read().rstrip())
time = list(map(int, read().split()))
time.sort()
result1 = 0
result2 = []
for i in time:
    result1 += i
    result2.append(result1)
print(sum(result2))