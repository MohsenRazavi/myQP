"""
x: total weight of elevator
weights: weights of people

num of subsets of an array is 2^n however its permutations are n! so we prefer to use subsets

dp is a 2D array which contains these information for every subset: [minimum number of rides, minimum last ride allocated space]
s is the subset mask
with p we check the elements which are in mask (using indexes)
s ^ (1 << p) gives us the last state of this subset and we stored it in dp array
at the end we have the answer of problem in dp[-1][0]
https://www.youtube.com/watch?v=UEkvzjsodDk
"""

x = int(input())
weights = [int(i) for i in input().split()]

n = len(weights)
dp = [[0, 0] for _ in range(1 << n)]
dp[0] = [1, 0]


def find_optimum_ans():
    for s in range(1, 1 << n):
        # initial value: n+1 rides are needed
        dp[s] = [n + 1, 0]
        for p in range(n):
            if s & (1 << p):
                option = dp[s ^ (1 << p)]
                if option[1] + weights[p] <= x:
                    # add p to an existing ride
                    option = [option[0], option[1] + weights[p]]
                else:
                    # reserve a new ride for p
                    option = [option[0] + 1, weights[p]]
                dp[s] = min(dp[s], option)
    return dp[-1][0]
