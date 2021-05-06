# 1 1                             1   1     2
# 1 2 / 2 1                       2   3     1
# 3 1 / 2 2 / 1 3                 3   6     2
# 1 4 / 2 3 / 3 2 / 4 1           4   10    1
n = int(input())
first_n = n
row_num, cnt = 1, 0
last_num = 0
result = [0,0]

while True:
    n -= row_num
    if n <= 0:
        break
    last_num += row_num
    row_num += 1
last_num = first_n -last_num
    
a = list(range(1,row_num+1))
b = list(range(row_num, 0, -1))
    
for j,k in zip(a,b):
    if row_num%2 == 0:
        result = [j,k]
    else:
        result = [k,j]

    cnt += 1
    if cnt == last_num:
        break

print(f'{result[0]}/{result[1]}')