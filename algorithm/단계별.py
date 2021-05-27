import sys; read = sys.stdin.readline

n = int(read())
info = [[read().split(),i] for i in range(n)]
# info = [
#     [[1, 'a'],0],
#     [[2, 'a'],1],
#     [[3, 'a'],2],
#     # [[20, 'Sunyoung'],2],
# ]
info = sorted(info, key=lambda x: (int(x[0][0]), int(x[1])))
for i in info:
    print(i[0][0], i[0][1])