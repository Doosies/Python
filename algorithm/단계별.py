max_num = 10000
n = int(input())
input_list = [int(input())for _ in range(n)]
count_list = [0 for _ in range(max_num)]
output_list = input_list.copy()
 
for i in input_list:
    count_list[i] += 1

for i,v in enumerate(count_list[1:]):
    count_list[i] += count_list[i-1]


for i in input_list:
    count_list[i] -= 1
    now_pos = count_list[i]
    output_list[now_pos] = i

print("\n".join(map(str,output_list)))