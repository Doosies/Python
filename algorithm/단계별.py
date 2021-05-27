import sys; read = sys.stdin.readline

cnt = [0 for _ in range(10)]
n = read().rstrip()

for i in n:
    cnt[int(i)] += 1
    
for i in range(9,-1,-1):
    for j in range(cnt[i]):
        print(i,end='')