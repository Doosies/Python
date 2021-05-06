i = 1
x = int(input()) - i
while True:
    if x <= 0:
        break
    x -= i * 6
    i += 1
print(i)