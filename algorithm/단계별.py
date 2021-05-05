a, b, c = list(int(input()) for _ in range(3))
result = str(a * b * c)
for i in range(10):
    print(result.count(f'{i}'))
