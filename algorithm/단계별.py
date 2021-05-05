n = list(int(input()) for _ in range(9))
maxNum = max(n)
print(maxNum)
print(n.index(maxNum)+1)