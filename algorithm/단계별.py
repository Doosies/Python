ll = []
for i in range(1,10001,1):
    add = int(i)
    for j in str(i):
        add += int(j)
    ll.append(add)
for i in range(1,10001,1):
    if i not in ll:
        print(i)