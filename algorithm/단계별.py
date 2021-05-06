import math

a, b, c = map(int, input().split())

# 10 - 2 + 1
# a,b,c = [5,1,6]
print(math.ceil((c-a)/(a-b))+1)
# now = 0
# day = 0

# while True:
#     day += 1
#     now += a
#     if now >= c:
#         break
#     now -= b
# print(day)

