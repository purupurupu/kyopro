H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# directions: right, down, right-down, left-down, left, up, left-up, right-up
dx = [0, 1, 1, 1, -1, -1, -1, -1]
dy = [1, 0, 1, -1, -1, 0, 1, 1]

target = list("snuke")

positions = []

for x in range(H):
    for y in range(W):
        if S[x][y] == target[0]:  # If the cell starts with 's'
            for direction in range(8):  # Check 8 directions
                for i in range(5):  # Check 5 consecutive cells
                    nx, ny = x + dx[direction]*i, y + dy[direction]*i
                    if nx < 0 or H <= nx or ny < 0 or W <= ny:  # If it's out of the grid
                        break
                    if S[nx][ny] != target[i]:  # If the cell does not match the target
                        break
                else:  # If 'snuke' is found
                    for i in range(5):
                        # save the positions
                        positions.append(
                            (x + dx[direction]*i + 1, y + dy[direction]*i + 1))

for pos in positions:
    print(*pos)
