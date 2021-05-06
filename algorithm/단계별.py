# 1 1                             1   1     2
# 1 2 / 2 1                       2   3     1
# 3 1 / 2 2 / 1 3                 3   6     2
# 1 4 / 2 3 / 3 2 / 4 1           4   10    1
n = int(input())
max_num = 0
line = 0
# result = [0,0]

while n > max_num:
    line += 1
    max_num += line
now_col = max_num - n 

if line % 2 == 0:
    top = line - now_col
    bot = now_col + 1
else:
    top = now_col + 1
    bot = line - now_col

print(f'{top}/{bot}')   