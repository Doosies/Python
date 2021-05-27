import sys; read = sys.stdin.readline
from collections import Counter

n = int(read()) # 입력되는값, 홀수
num_li = sorted([int(read()) for _ in range(n)])
cnt = Counter(num_li).most_common(2)

print(round(sum(num_li) / n))
print(num_li[n//2])
print(cnt[-1][0] if cnt[0][1] == cnt[-1][1]  else cnt[0][0])
print(max(num_li)-min(num_li))
