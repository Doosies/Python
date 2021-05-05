n = int(input())
cnt = 0

def isSeq(num):
    num = (str(num))
    plus = set()
    
    for j in range(len(num) -1 ,0,-1):
        r = int(num[j]) - int(num[j-1])
        plus.add(r)
    return True if len(plus) == 1 else False

for i in range(1,n+1):
    if isSeq(i) == True or i < 100:
        cnt +=1
print(cnt)