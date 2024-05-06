from math import log2, floor


def preprocess(arr):
    length = len(arr)
    min_arr = [[i for i in arr]]
    max_range = floor(log2(length))
    for l in range(1, max_range+2):
        min_sub_arr = []
        for i in range(len(min_arr[-1])-l):
            min_sub_arr.append(min(min_arr[-1][i], min_arr[-1][i+l]))
        min_arr.append(min_sub_arr)

    return min_arr


def min_sparse_table(arr, a, b):
    min_preprocess_table = preprocess(arr)
    print(min_preprocess_table)
    k = floor(log2(b-a+1))
    return min(min_preprocess_table[k][a], min_preprocess_table[k][b-2**k+1])


print(min_sparse_table([1, 4, 2, 3, 5, 2, 6, 8, 0, 7], 5, 7))



