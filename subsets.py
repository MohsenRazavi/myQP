
arr = [1, 2, 3]
subset = []

def get_subsets(k, subset):
    """
    This function generates all subsets of a given set.
    It takes an integer k and a list subset as parameters and does not return any value.
    Time Complexity: O(2^n * n)
    """
    if k == len(subset):
        print(subset)
    else:
        get_subsets(k+1, subset)
        subset.append(k)
        get_subsets(k+1, subset)
        subset.pop()



def get_subsets_bitwise():
    """
    Generates all possible subsets of the input array using bitwise operations.
    In the first loop we make all the subsets representations in binary (ex. from 0b0000 to 0b1111) 
    In This representation, appearance of 0 index of array will be shown by setting the last bit 1 and ... 
    In the second loop we add the value of specified index into a subset.
    Time Complexity: O(2^n * n)
    """
    for i in range(1<<len(arr)):
        subset = []
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
        print(subset)



get_subsets_bitwise()
