from math import log2


def make_segment_tree(arr):
    l = len(arr)
    ll = log2(l)
    if ll != int(ll):
        k = 2
        while k < l:
            k *= 2
        for i in range(k - l):
            arr.append(0)
        l = k
    segment_tree = [0 for _ in range(l)]
    segment_tree += arr
    for i in range(2 * l - 1, 1, -2):
        segment_tree[i // 2] = segment_tree[i] + segment_tree[i - 1]

    return segment_tree


def sum_segment_tree(a, b, stree):
    n = len(stree) // 2
    a += n
    b += n
    s = 0
    while a <= b:
        if a % 2 == 1:
            s += stree[a]
            a += 1
        if b % 2 == 0:
            s += stree[b]
            b -= 1
        a //= 2
        b //= 2
    return s


def segment_tree_update(k, x, stree):
    """
    update kth index by increasing x units
    """
    k += len(stree)//2
    stree[k] += x
    k //= 2
    while k >= 1:
        stree[k] = stree[2*k] + stree[2*k+1]
        k //= 2



