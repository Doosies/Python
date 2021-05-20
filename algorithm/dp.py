n = int(input())
def is_666(string):
    string = str(string)
    for i in range(len(string)):
        if i + 2 <len(string):
            if string[i] == '6' and string[i+1] == '6' and string[i+2] == '6':
                return True
    return False

now_num = 665
cnt = 0
result = []
while True:
    if cnt == n:
        break
    

    if is_666(now_num + 1):
        result.append(now_num +1)
        cnt += 1
        now_num += 1
    elif str(int(now_num+1/19))[-1] == '6':
        while True:
            now_num += 1
            if is_666(now_num):
                result.append(now_num)
                cnt += 1
                break
    elif is_666(now_num + 1000):
        result.append(now_num + 1000)
        cnt += 1
        now_num += 1000
    else:
        now_num += 1

print(result[n-1])