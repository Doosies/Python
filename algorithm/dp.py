import sys; read = sys.stdin.readline()
n = int(read)
print((2**n)-1)

def solve(n, start, to, via):
    if n == 1:
        print("종료", start, to)
        return
    else:
        solve(n-1, start, via, to)
        print("진행", start, to)
        solve(n-1, via, to, start)
solve(n,1,3,2)



