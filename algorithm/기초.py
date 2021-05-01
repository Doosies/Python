n = int(input())

# m = int(input())
# h, m = map(int, input().split())

for i in reversed(range(n)):
    print('{}{}'.format(' ' * (i), '*' * (n-i)))