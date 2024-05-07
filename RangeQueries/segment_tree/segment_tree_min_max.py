
from math import log2


def make_segment_tree(arr, func):
    l = len(arr)
    ll = log2(l)
    if ll != int(ll):
        k = 2
        while k < l:
            k *= 2
        if func == min:
            value = float('inf')
        else:
            value = float('-inf')
        for i in range(k - l):
            arr.append(value)
        l = k
    segment_tree = [0 for _ in range(l)]
    segment_tree += arr
    for i in range(2 * l - 1, 1, -2):
        segment_tree[i // 2] = func(segment_tree[i], segment_tree[i - 1])

    return segment_tree

