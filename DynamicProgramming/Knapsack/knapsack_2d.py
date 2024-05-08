"""
weights is array of weights
k is number of items (length of weight)
we will construct a 2D list named possible[k][x] which says that we can make sum of x by using k first weights or not
"""


def check_possibility():
    for k in range(1, n + 1):
        for x in range(m + 1):
            if x - weights[k - 1] >= 0:
                possible[k][x] |= possible[k - 1][x - weights[k - 1]]
            possible[k][x] |= possible[k - 1][x]
    return possible[n][m]


target_sum = int(input())
weights = [int(i) for i in input().split()]
n = len(weights)
m = sum(weights)

possible = [[False for _ in range(m + 1)] for _ in range(n + 1)]
possible[0][0] = True

check_possibility()
