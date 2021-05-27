import sys; read = sys.stdin.readline
from itertools import permutations

n,m = map(int, read().split())
p = [str(i) for i in range(1, n+1)]
for sq in permutations(p,m):
    print(' '.join(sq))