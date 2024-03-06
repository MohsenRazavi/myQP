
def counting_sort(arr):
    n = max(arr)
    counting_arr = n * [0]
    for i in arr:
        counting_arr[i] += 1
    
    res = []
    for i in range(n):
        for _ in range(counting_arr[i]):
            res.append(i)
    
    return res

