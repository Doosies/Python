import sys; read = sys.stdin.readline

n = int(read())
pos = [list(map(int,read().split())) for _ in range(n)]

for i in sorted(pos, key=lambda x: (x[0], x[1])):
    print(i[0], i[1])