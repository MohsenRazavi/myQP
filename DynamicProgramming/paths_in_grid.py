

def find_path(grid, func):
    x = len(grid)
    y = len(grid[0])
    max_paths = [[0 for _ in range(y)] for _ in range(x)]

    grid = [0]*y + grid
    for row in grid:
        row = [0]+row
    for i in range(x):
        for j in range(y):
            max_paths[i][j] = max(grid[i][j-1], grid[i-1][j]) + grid[i][j]
