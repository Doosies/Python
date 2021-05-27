import sys; read = sys.stdin.readline
from itertools import permutations, combinations, product

n, m = map(int, read().split())
def solve(now):
    if len(now) >= m:
        print(" ".join(map(str,now)))
        return
    for i in range(1,n+1):
        if len(now) == 0 or i >= now[-1]:
            now.append(i)
            solve(now)
            now.pop()
solve([])
