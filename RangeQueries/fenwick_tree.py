"""
fenwick tree or binary index tree
kth fenwick tree index stores sum of (k & -k) last elements in it
"""


def fenwick_sum(k, ftree):
    s = 0
    while k >= 1:
        s += ftree[k]
        k -= k & -k

    return s


def fenwick_update(i, x, ftree):
    """
    this function updates index ith of the tree by increasing it by x
    """
    while i <= len(ftree):
        ftree[i] += x
        i += i & -i


def make_fenwick(arr):
    l = len(arr)
    fenwick = [0 for _ in range(l)]
    fenwick[0] = arr[0]
    for i in range(1, l):
        k = (i+1) & -(i+1)
        s = arr[i]
        j = 1
        while j < k:
            s += fenwick[i-j]
            j += (i-j+1) & -(i-j+1)
        fenwick[i] = s

    return fenwick

