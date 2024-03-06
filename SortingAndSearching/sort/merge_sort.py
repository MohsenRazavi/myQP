
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    left_arr = arr[:n//2]
    right_arr = arr[n//2:]

    sorted_left_arr = merge_sort(left_arr)
    sorted_right_arr = merge_sort(right_arr)

    a = len(sorted_left_arr)
    b = len(sorted_right_arr)
    x = y = 0
    sorted_merged_arr = []
    while x < a and y < b:
        if sorted_right_arr[x] < sorted_left_arr[y]:
            sorted_merged_arr.append(sorted_right_arr[x])
            x += 1
        elif sorted_right_arr[x] > sorted_left_arr[y]:
            sorted_merged_arr.append(sorted_left_arr[y])
            y += 1
        else:
            sorted_merged_arr.append(sorted_left_arr[y])
            sorted_merged_arr.append(sorted_right_arr[x])
            x += 1
            y += 1
    
    while x < a:
        sorted_merged_arr.append(sorted_right_arr[x])
        x += 1
    
    while y < b:
        sorted_merged_arr.append(sorted_left_arr[y])
        y += 1

    return sorted_merged_arr


