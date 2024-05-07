

def lis_length(arr):
    l = len(arr)
    lis = [1] * l
    for i in range(l):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j]+1)

    return max(lis)




