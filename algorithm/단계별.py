n = int(input())
subject_list = list(map(int, input().split()))
max_num = max(subject_list)
new_subject_list = [val/max_num*100 for val in subject_list]
print(sum(new_subject_list) / len(new_subject_list))
