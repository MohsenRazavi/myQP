
def find_mex(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > i:
            return i
    return i+1
        
