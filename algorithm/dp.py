# n = int(input())
n = int(input())
li = [[' '] * n for _ in range(n)]

def solve(y, x, size):
    if size == 1:
        li[y][x] = '*'
        return
    div = size // 3
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += 1
            if cnt != 5:
                solve( y+i*div, x+j*div, div)


solve(0,0,n)
for y in range(n):
    for x in range(n):
        print(li[y][x], end='')
    print()