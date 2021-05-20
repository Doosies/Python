import time
n = int(input())
start = time.time()
def is_666(string):
    string = str(string)
    if string.count('6') >= 3:
        for i in range(len(string)):
            if i + 2 <len(string):
                if string[i] == '6' and string[i+1] == '6' and string[i+2] == '6':
                    return True
    return False

now_num = 665
cnt = 0
result = []
# test = [
# 666,1666,2666,3666,4666,5666,6660,6661,6662,6663,
# 6664,6665,6666,6667,6668,6669,7666,8666,9666]
while True:
    if cnt == n:
        break

    if str(int(now_num+1/19))[-1] == '6':
        while True:
            now_num += 1
            if is_666(now_num):
                result.append(now_num)
                cnt += 1
                break
    # else:
        
    elif is_666(now_num + 1):
        result.append(now_num +1)
        cnt += 1
        now_num += 1
    elif is_666(now_num + 1000):
        result.append(now_num + 1000)
        cnt += 1
        now_num += 1000
    else:
        now_num += 1

for i in result:
    print(i)
print("end: ", time.time() - start)