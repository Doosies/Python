import sys; read = sys.stdin.readline

n = int(read().rstrip())
num = [int(read().rstrip()) for _ in range(n)]
# num = [6, 5, 3, 1, 8, 7, 2, 4, 9,10]

def merge(left, right):
    sorted_li = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_li.append(left[left_idx])
            left_idx += 1
        else:
            sorted_li.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        sorted_li.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_li.append(right[right_idx])
        right_idx += 1

    return sorted_li

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
    

a = merge_sort(num)
print("\n".join(map(str,a)))
