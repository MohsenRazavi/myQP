
arr = [1, 2, 3]
n = len(arr)
permutation = []
chosen = [None for _ in range(n)]
def get_permutations():
    """
    Recursive function to generate all permutations of a given list of elements.
    At each state chooses one of the elements and at the next state chooses another element.
    """
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(n):
            if chosen[i]:
                continue
            chosen[i] = True
            permutation.append(i)
            get_permutations()
            chosen[i] = False
            permutation.pop()



from itertools import permutations

perm = permutations([1, 2, 3])
for i in list(perm):
    print(i)

