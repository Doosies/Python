import sys; read = sys.stdin.readline

n, k = map(int, read().split())
a = [int(read().rstrip()) for _ in range(n)]

# n, k = [10, 4790]
# a = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
cnt = 0

for i in reversed(a):
    while i <= k:
        cnt += k // i
        k = k % i
print(cnt)