# t개의 테스트 데이터
# h 층수
# w 방개수, w는 필요없어
# n 번째 도착 손님
import math
t = int(input())
t2 = [list(map(int,input().split())) for _ in range(t)]

for h,w,n in t2:
    result_w = str(math.ceil(n/h))
    result_h = h if n % h == 0 else n % h
    if len(result_w) == 1:
        result_w = '0'+result_w
    print(f'{result_h}{result_w}')

