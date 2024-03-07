
def binary_search(arr, x):
    arr.sort()
    a = 0
    b = len(arr)-1
    
    while a <= b:
        key_index = (a+b) // 2
        key = arr[key_index]

        if x == key:
            return True, key_index
        elif x > key:
            a = key_index + 1
        else:
            b = key_index - 1

    return False




arr = [1, 2, 3, 4, 2, 3, 5, 8, 9, 1, 10, 15]

print(binary_search(arr, 15))