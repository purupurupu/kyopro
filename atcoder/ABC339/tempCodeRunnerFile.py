from collections import deque

def find_positions(grid, N):
    positions = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'P':
                positions.append((i, j))
    return positions

def bfs(start1, start2, N, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    visited.add((start1, start2))
    queue = deque([(start1, start2, 0)])  # (position1, position2, moves)

    while queue:
        (x1, y1), (x2, y2), moves = queue.popleft()

        # 同一地点
        if x1 == x2 and y1 == y2:
            return moves

        for dx, dy in directions:
            new_x1, new_y1 = x1 + dx, y1 + dy
            new_x2, new_y2 = x2 + dx, y2 + dy

            if not (0 <= new_x1 < N and 0 <= new_y1 < N) or grid[new_x1][new_y1] == '#':
                new_x1, new_y1 = x1, y1

            if not (0 <= new_x2 < N and 0 <= new_y2 < N) or grid[new_x2][new_y2] == '#':
                new_x2, new_y2 = x2, y2

            if ((new_x1, new_y1), (new_x2, new_y2)) not in visited:
                visited.add(((new_x1, new_y1), (new_x2, new_y2)))
                queue.append(((new_x1, new_y1), (new_x2, new_y2), moves + 1))

    return -1

N = int(input())
S = [input() for _ in range(N)]

positions = find_positions(S, N)

res = bfs(positions[0], positions[1], N, S)
print(res)


