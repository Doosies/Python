# h = int(input())
# m = int(input())
h, m = map(int, input().split())
t = (h*60) + m - 45
h2 = t // 60
m2 = t % 60
if h2 < 0:
    h2 += 24
print(h2, m2)