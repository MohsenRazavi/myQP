def mex(arr):
    arr.sort()
    mex = 0
    for i in range(len(arr)):
        if arr[i] == mex:
            mex += 1
    return mex