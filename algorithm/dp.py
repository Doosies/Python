m, n = map(int, input().split())
board = [input() for _ in range(m)]

# m, n = 8, 8
# board = """WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW"""
# m, n = 10, 13
# board = """BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB"""


board = board.split("\n")
result = m*n
# def func(check_val, a, b, k, l):
#     cnt = 0
#     if k % 2 == 0:
#         if l % 2 == 0:
#             if check_val != a: cnt += 1
#         else:
#             if check_val != b: cnt += 1
#     else:
#         if l % 2 == 0:
#             if check_val != b: cnt += 1
#         else:
#             if check_val != a: cnt += 1
    
#     return cnt

for i in range(m-8 +1):
    for j in range(n-8 +1):
        cnt1 = 0
        cnt2 = 0

        for k in range(i,i+8):
            if k % 2 == 0:
                tmp1 = 'W'
                tmp2 = 'B'
            else:
                tmp1 = 'B'
                tmp2 = 'W'
                
            for l in range(j,j+8):
                now = board[k][l]
                if l % 2 == 0:
                    if now != tmp1: cnt1+=1
                    if now != tmp2: cnt2+=1
                else:
                    if now == tmp1: cnt1+=1
                    if now == tmp2: cnt2+=1
                
        result = min(result, min(cnt1, cnt2))
print(result)


# 1. 만약 맨 위가 w면 
#     k 짝수 - #wbwbwbwb
#         l 짝수 - w
#         l 홀수 - b
#     k 홀수 - bwbwbwbw
#         l 짝수 - b
#         l 홀수 - w
# 2. 만약 맨 위가 b면
#     k 짝수 - # bwbwbwbw
#         l 짝수 - b
#         l 홀수 - w
#     k 홀수 - #wbwbwbwb
#         l 짝수 - w
#         l 홀수 - b