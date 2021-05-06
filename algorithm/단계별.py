a, b, c = map(int, input().split())
a = a / (c-b) + 1 if c > b else -1
print(int(a))