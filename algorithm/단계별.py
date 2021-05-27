import sys; read = sys.stdin.readline
from itertools import permutations, combinations


def solv(now):
    if len(now) >= m:
        print(" ".join(map(str,now)))
        return now
    for i in range(1, n+1):
        if i not in now and (len(now) == 0 or i >= now[-1]):
            now.append(i)
            solv(now)
            now.pop()

n, m = map(int, read().split())
solv([])