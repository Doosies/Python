import sys
read = sys.stdin.readline


gg = list(range(0,9999))
gg = [str(val).zfill(3) for val in gg]
rst = []
for i in gg :
    for idx in range(len(i)+1):
        li = list(i)
        li.insert(idx,'666')
        rr = int( ''.join(li) )
        rst.append(rr)

rst = list(set(rst))
rst.sort()
N = int(read())
print(rst[N-1])