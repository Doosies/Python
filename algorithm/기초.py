n = input()
first = n
result = 0
cnt = 0

while True:
    if len(n) == 1:
        n = '0' + n

    result = str( int(n[0])+int(n[1]) )
    n = n[1] + result[len(result)-1]
    cnt += 1

    if int(n) == int(first):
        break
print(cnt)