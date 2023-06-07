H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


# マス目の文字列を2次元リストとして受け取る
grid = []
for _ in range(H):
    row = list(input().strip())
    grid.append(row)

# s, n, u, k, e の順に連続している場所を探す
for i in range(H):
    for j in range(W):
        # if grid[i][j] == 's':
        #     s = (i, j)
        # elif grid[i][j] == 'n':
        #     n = (i, j)
        # elif grid[i][j] == 'u':
        #     u = (i, j)
        # elif grid[i][j] == 'k':
        #     k = (i, j)
        # elif grid[i][j] == 'e':
        #     e = (i, j)
        if grid[i][j] == 's':
            s = (i, j)
            if grid[i-1][j] == 'n' or grid[i+1][j] == 'n' or grid[i][j-1] == 'n':
