n = int(input())
check_row = [False] * n
check_left_up = [False] * (2*n -1)
check_right_up = [False] * (2*n -1)
cnt = 0

def chess(row):
    if row == n:
        global cnt
        cnt += 1
        return
    for col in range(n):
        if (not check_row[col] 
        and not check_left_up[(n-1)+(row-col)]
        and not check_right_up[(row+col)]):
            check_row[col] = check_left_up[(n-1)+(row-col)] = check_right_up[row+col] = True
            chess(row+1)
            check_row[col] = check_left_up[(n-1)+(row-col)] = check_right_up[row+col] = False

chess(0)
print(cnt)