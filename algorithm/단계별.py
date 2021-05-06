n = int(input())
st_list = list(input() for _ in range(n))
cnt = 0

for string in st_list:
    no = False
    for i,one in enumerate(string):
        count = string[:i].count(one)
        if i > 0 and count >= 1:
            if string[i-1] != one:
                no = True
                break
    if no == False:
        cnt += 1
print(cnt)
    

    


