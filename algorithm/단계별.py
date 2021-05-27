import sys; read = sys.stdin.readline
from itertools import permutations, combinations, product

n, m = map(int, read().split())
# pool = [str(i) for i in range(1,n+1)]
# for i in combinations (pool, m):
#     print(" ".join(i))

def solv(now):
    if len(now) >= m:
        print(' '.join(now))
        return now
    for i in range(1, n+1):
        now.append(str(i))
        solv(now)
        now.pop()
solv([])