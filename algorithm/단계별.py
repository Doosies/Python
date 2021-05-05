ll = set(range(1,10001))
rm = set()

for i in ll:
    add = int(i)
    for j in str(i):
        add += int(j)
    rm.add(add)
result = ll - rm
for num in sorted(result):
    print(num)
