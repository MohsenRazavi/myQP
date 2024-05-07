

target_sum = int(input())
weights = [int(i) for i in input().split()]
n = len(weights)
m = sum(weights)

possible = [False for _ in range(m)]
possible[0] = True

for k in range(n):
    for x in range(m-weights[k], 0, -1):
        possible[x+weights[k]] |= possible[x]
