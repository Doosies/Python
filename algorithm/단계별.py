t = int(input())
inp = [int(input()) for _ in range(t)]
max_inp = max(inp)

prime = [True] * (max_inp+1)
prime[1] = False

for i in range( 2, int(max_inp**0.5)+1):
    if prime[i]:
        for j in range( i*2, max_inp+1, i):
            prime[j] = False

for i in inp:
    now = prime[:i+1]
    primes = [j for j in range(1,i+1) if now[j]== True]
    half = int(len(primes)/2) - 1
    before_minus = i*2
    before_li = []
    for j in range(half, len(primes)):
        minus = i - primes[j]
        now_prime = primes[j]
        if minus in primes:
            now = [minus, now_prime]
            sort_now = [min(now), max(now)]
            if sort_now[1] - sort_now[0] >= before_minus:
                print(before_li[0], before_li[1])
                break
            elif sort_now[0]==sort_now[1]:
                print(sort_now[0], sort_now[1])
                break
            before_minus = sort_now[1] - sort_now[0]
            before_li = sort_now