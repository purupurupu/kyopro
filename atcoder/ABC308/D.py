H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
char_to_index = {char: i for i, char in enumerate('snuke')}
found = [[0]*W for _ in range(H)]
found[0][0] = 1
queue = [(0, 0)]

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or H <= nx or ny < 0 or W <= ny:
            continue
        if grid[nx][ny] == 'snuke'[found[x][y] % 5] and not found[nx][ny]:
            found[nx][ny] = found[x][y] + 1
            queue.append((nx, ny))

print('Yes' if found[H-1][W-1] else 'No')
