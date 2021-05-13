import sys

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())
    d = ((x2 - x1)**2 +(y1 - y2)**2)**0.5
    ab = abs(r1-r2)
    
    if r1 + r2 < d or ab > d:
        print(0)
    elif d == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 == d or ab == d:
        print(1)
    else:
        print(2)