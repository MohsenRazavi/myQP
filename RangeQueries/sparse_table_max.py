from math import log2, floor


def preprocess(arr):
    length = len(arr)
    max_arr = [[i for i in arr]]
    max_range = floor(log2(length))
    for l in range(1, max_range + 2):
        max_sub_arr = []
        for i in range(len(max_arr[-1]) - l):
            max_sub_arr.append(max(max_arr[-1][i], max_arr[-1][i + l]))
        max_arr.append(max_sub_arr)

    return max_arr


def max_sparse_table(arr, a, b):
    max_preprocess_table = preprocess(arr)
    print(max_preprocess_table)
    k = floor(log2(b - a + 1))
    return max(max_preprocess_table[k][a], max_preprocess_table[k][b - 2 ** k + 1])


print(max_sparse_table([1, 4, 2, 3, 5, 2, 6, 8, 0, 7], 5, 7))
