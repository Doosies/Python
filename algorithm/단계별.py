import sys; read = sys.stdin.readline
from itertools import permutations, combinations

n, m = map(int, read().split())
pool = [str(i) for i in range(1,n+1)]
for i in combinations (pool, m):
    print(" ".join(i))