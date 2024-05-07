def make_difference_array(arr):
    difference_array = [arr[0]]
    for i in range(1, len(arr)):
        difference_array.append(arr[i] - arr[i - 1])
    return difference_array


def update_difference_array(a, b, x, darr):
    """
    increase difference array elements from ath index to bth index by x
    """
    darr[a] += x
    darr[b + 1] -= x


def get_original_array(darr):
    original_arr = [darr[0]]
    for i in range(1, len(darr)):
        original_arr.append(original_arr[i - 1] + darr[i])
    return original_arr
