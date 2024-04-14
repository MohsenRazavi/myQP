def preprocess(arr):
    lh = len(arr)
    lw = len(arr[0])
    sum_arr = [[0 for _ in range(lw)] for _ in range(lh)]
    for i in range(lh):
        for j in range(lw):
            s = 0
            for k in range(i+1):
                for h in range(j+1):
                    s += arr[k][h]

            sum_arr[i][j] = s

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




