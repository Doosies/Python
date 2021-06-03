import sys; read = sys.stdin.readline

n = int(read().rstrip())
table = [list(map(int,read().split())) for _ in range(n)]
start = 0
cnt = 0
for i in sorted(table,key=lambda x:(x[1],x[0])):
    if i[0] >= start:
        start = i[1]
        cnt += 1
print(cnt)