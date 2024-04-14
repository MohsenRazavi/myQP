
def preprocess(arr):
    sum_arr = []
    for i in range(len(arr)):
        s = 0
        for j in range(i+1):
            s += arr[j]

        sum_arr.append(s)

    return sum_arr


def prefix_sum(arr, start_index, end_index):
    sum_arr = preprocess(arr)
    return sum_arr[end_index] - sum_arr[start_index-1]

