H, W, N = map(int, input().split())

grid = [['.' for _ in range(W)] for _ in range(H)]
direction = 0
x, y = 0, 0

for _ in range(N):
    if grid[x][y] == '.':
        grid[x][y] = '#'
        direction = (direction + 1) % 4
    else:
        grid[x][y] = '.'
        direction = (direction - 1) % 4
    
    # move to next cell
    if direction == 0:  # up
        x = (x - 1) % H
    elif direction == 1:  # right
        y = (y + 1) % W
    elif direction == 2:  # down
        x = (x + 1) % H
    else:  # left
        y = (y - 1) % W

for row in grid:
    print(''.join(row))
