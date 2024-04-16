def preprocess(arr):
    lh = len(arr)
    lw = len(arr[0])
    sum_arr = [[0 for _ in range(lw)] for _ in range(lh)]
    sum_arr[0][0] = arr[0][0]
    for i in range(1, lw):
        sum_arr[0][i] = sum_arr[0][i-1] + arr[0][i]

    for j in range(1, lh):
        sum_arr[j][0] = sum_arr[j-1][0] + arr[j][0]

    for k in range(1, lh):
        for h in range(1, lw):
            sum_arr[k][h] = arr[k][h] + sum_arr[k-1][h] + sum_arr[k][h-1] - sum_arr[k-1][h-1]

    return sum_arr


def prefix_sum_2dimension(arr, start_position, end_position):
    sum_arr = preprocess(arr)
    ans = sum_arr[end_position[0]][end_position[1]]
    if 0 not in start_position:
        ans -= sum_arr[start_position[0] - 1][end_position[1]]
    if 0 not in end_position:
        ans -= sum_arr[end_position[0]][start_position[1] - 1]
    if 0 not in start_position and 0 not in end_position:
        ans += sum_arr[start_position[0] - 1][start_position[1] - 1]

    return ans


print(preprocess([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


