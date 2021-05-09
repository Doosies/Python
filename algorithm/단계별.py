import math

t = int(input())
points = [list(map(int,input().split()))for _ in range(t)]

for point in points:
    dist = point[1]-point[0]
    sqt = round(math.sqrt(dist))
    cnt = int((sqt * 2) -1)
    dist -= sqt ** 2

    while dist > 0:
        if dist - sqt >= 0:
            dist -= sqt
            cnt += 1
        else:
            sqt -= 1
    print(cnt)
