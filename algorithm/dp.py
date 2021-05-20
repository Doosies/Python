import sys; read = sys.stdin.readline

n = int(read().rstrip())
num = [int(read().rstrip()) for _ in range(n)]
num = sorted(num)
print("\n".join(map(str,num)))