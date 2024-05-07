from math import log2, floor


def preprocess(arr, func):
    length = len(arr)
    sparse_arr = [[i for i in arr]]
    max_range = floor(log2(length))
    for l in range(1, max_range + 2):
        sub_arr = []
        for i in range(len(sparse_arr[-1]) - l):
            sub_arr.append(func(sparse_arr[-1][i], sparse_arr[-1][i + l]))
        sparse_arr.append(sub_arr)

    return sparse_arr


def max_sparse_table(arr, a, b, func):
    """
    arr: original array
    a: start of range
    b: end of range
    func: min or max function
    """
    preprocess_table = preprocess(arr, func)
    print(preprocess_table)
    k = floor(log2(b - a + 1))
    return func(preprocess_table[k][a], preprocess_table[k][b - 2 ** k + 1])



