
def preprocess(arr):
    sum_arr = [arr[0]]
    for i in range(1, len(arr)):
        sum_arr.append(sum_arr[i-1] + arr[i])
    return sum_arr


def prefix_sum(arr, start_index, end_index):
    sum_arr = preprocess(arr)
    return sum_arr[end_index] - sum_arr[start_index-1]

