sum = 0
n = input().upper()
l = [[],[],[],
     ['A','B','C'],['D','E','F'],['G','H','I'],
     ['J','K','L'],['M','N','O'],['P','Q','R','S'],
     ['T','U','V'],['W','X','Y','Z']
    ]
for string in n:
    for i,v in enumerate(l):
        if string in v:
            sum += i
            break
print(sum)