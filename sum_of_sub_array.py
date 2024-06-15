
arr = [1, 2, 3, 4, 3, 6, 1, 7, 2]
s = 10

a = 0
b = 0

sub_arrays = []

while a <= b:
    if a == b == len(arr):
        break
    elif a == b:
        b += 1
    elif b == len(arr):
        a += 1
        b = a + 1
    else:
        b += 1 
    if sum(arr[a:b]) == s:
        sub_arrays.append(arr[a:b])

if sub_arrays:
    for sub_array in sub_arrays:
        print(sub_array)
else:
    print('Not Found !')

