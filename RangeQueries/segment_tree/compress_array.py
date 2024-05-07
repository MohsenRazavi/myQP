
def compressor(arr, needed_indexes):
    compressed_arr = []
    needed_indexes.sort()
    for index in needed_indexes:
        compressed_arr.append(arr[index])

    return compressed_arr
