n = int(input())
n_len = len(list(str(n)))

result = 0
start = 0
if n >= 18:
    start = int(n - n_len * 9)



for i in range(start, n-1):
    num = list(str(i))
    num = list(map(int,num))
    if n == sum(num) + i:
        result = i
        break

print(result)