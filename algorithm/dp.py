n, m = map(int, input().split())
cards = list(map(int, input().split()))
# n, m = 5, 21
# cards = 5, 6, 7, 8, 9
result = []

for i,v in enumerate(cards):
    for j in range(i):
        for k in range(j):
            re = cards[i]+cards[j]+cards[k]
            if re <= m:
                result.append(re)
print(max(result))


