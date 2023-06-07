def split_array_2d(array):
    n = len(array)
    # 横方向の分割
    horizontal = array[:]
    # 縦方向の分割
    vertical = [[array[j][i] for j in range(n)] for i in range(n)]
    # 斜め方向の分割
    diagonal = [[array[i][i]
                for i in range(n)], [array[i][n-1-i] for i in range(n)]]

    return horizontal, vertical, diagonal


H, W = map(int, input().split())

# マス目の文字列を2次元リストとして受け取る
grid = []
for _ in range(H):
    row = list(input().strip())
    grid.append(row)

horizontal_array, vertical_array, diagonal_array = split_array_2d(grid)

print(horizontal_array)
print(vertical_array)
print(diagonal_array)
