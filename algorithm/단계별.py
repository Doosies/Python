import sys; read = sys.stdin.readline
from itertools import permutations, combinations, product

n, m = map(int, input().split())
p = [str(i) for i in range(1,n+1)]
print("\n".join(map(" ".join, product(p, repeat=m))))