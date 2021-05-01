import sys
n, x = map(int, input().split())
a = map(int,sys.stdin.readline().split())
result = [str(val) for val in a if val < x]
print(" ".join(result))