import sys; read = sys.stdin.readline
city = int(read().strip())
dist = list(map(int, read().split()))
dist.append(0)
price = list(map(int, read().split()))

min_price = 1000000000
result = 0

for i in range(city):
    if price[i] < min_price:
        min_price = price[i]

    result += dist[i] * min_price

print(result)