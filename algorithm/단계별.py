import sys; read = sys.stdin.readline


n = int(read()) # 입력되는값, 홀수

num_li = [int(read()) for _ in range(n)]
num_li.sort()

cnt = {v:0 for v in num_li}
for i in num_li:
    cnt[i] += 1
max_key, max_cnt = max(cnt.items(),key=lambda x:x[1])
maxxxx = list(filter(lambda x: x[1] == max_cnt, cnt.items()))
if len(maxxxx) > 1:
    maxxxx = maxxxx[1][0]
else:
    maxxxx = maxxxx[0][0]

print(round(sum(num_li) / n))
print(num_li[n//2])
print(maxxxx)
print(max(num_li)-min(num_li))