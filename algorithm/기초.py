n = int(input())
add_list = []
# m = int(input())
# h, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    add_list.append(a+b)
for v in add_list:
    print(v)