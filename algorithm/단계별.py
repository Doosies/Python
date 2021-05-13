from math import sqrt, floor

inp = []
while True:
    n = int(input())
    if n == 0:
        break
    inp.append(n)

max_inp = max(inp)*2
prime = [True] * (max_inp+1)
for i in range( 2, int(max_inp**0.5)+1):
    if prime[i]:
        for j in range( i*2, max_inp, i):
            prime[j] = False

for i in inp:
    if i == 1:
        print("1")
    else:
        print(sum(prime[i+1:2*i]))
