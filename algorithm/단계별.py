n = int(input())
ox = list(input() for _ in range(n))

for i,v in enumerate(ox):
    before = ''
    now = ''
    score = 0
    plus = 1
    for val in ox[i]:
        now = val
        if val == 'O':
            plus = plus + 1 if before == 'O' else 1
            score += plus
        before = now
    print(score)