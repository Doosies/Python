n = int(input())
nl = []
# m = int(input())
# h, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    nl.append(a+b)
for i,v in enumerate(nl):
    print(f'Case #{i+1}: {v}')