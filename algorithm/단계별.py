C = int(input())
cases = list(list(map(int,input().split())) for _ in range(C))
for case in cases:
    avg = sum(case[1:]) / case[0]
    bigger = [score for score in case[1:] if score > avg]
    percentage = len(bigger) / case[0] * 100
    print(f'{percentage:0.3f}%')