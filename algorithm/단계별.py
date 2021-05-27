import sys; read = sys.stdin.readline

n = int(read())
num = list(map(int, read().split()))
num_dict = {v:i for i,v in enumerate(sorted(set(num)))}
for i in num:
    print(num_dict[i], end=' ')