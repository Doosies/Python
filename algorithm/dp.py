n = int(input())
inp = [input().split() for _ in range(n)]
rank = [1] * len(inp)
end = len(inp)

for i in range(end):
    for j in range(i+1,end):
        if inp[i][0] > inp[j][0] and inp[i][1] > inp[j][1]:
            rank[j] += 1
        elif inp[i][0] < inp[j][0] and inp[i][1] < inp[j][1]:
            rank[i] += 1

rank = " ".join([str(_) for _ in rank])
print(rank)