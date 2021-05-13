t = int(input())
inp = [int(input()) for _ in range(t)]
max_inp = max(inp)

prime = [True] * (max_inp+1)
prime[0] = False
prime[1] = False

for i in range( 2, int(max_inp**0.5)+1):
    if prime[i]:
        for j in range( i*2, max_inp+1, i):
            prime[j] = False

for number in inp:
    for i in range(number//2, number):
        if prime[i] and prime[number-i]:
            print(number-i, i)
            break