import sys

def find(num):
    if num[0] == num[1]:
        return num[2]
    elif num[1] == num[2]:
        return num[0]
    else:
        return num[1]

points = [sys.stdin.readline().split() for _ in range(3)]
x = [p[0] for p in points]
y = [p[1] for p in points]

print(find(x), find(y))