

target_sum = int(input())
weights = [int(i) for i in input().split()]
n = len(weights)
m = sum(weights)

possible = [False for _ in range(m+1)]
possible[0] = True

for k in range(n+1):
    for x in range(m-weights[k], 0, -1):
        possible[x+weights[k]] |= possible[x]

#TODO This code needs to be fixed !