import sys; read = sys.stdin.readline

n = int(read())
inp = [read().rstrip() for _ in range(n)]
inp = set(inp)
inp = sorted(inp, key=lambda x:( len(x), x[:]))
print("\n".join(inp))