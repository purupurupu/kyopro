def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    N = min(H, W)
    ans = [0] * (N + 1)

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i - 1][j - 1] == '#':
                for n in range(1, N + 1):
                    if is_batsu(grid, i, j, n):
                        ans[n] += 1

    print(*ans[1:])


def is_batsu(grid, a, b, n):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d in range(1, n + 1):
        for dx, dy in directions:
            x, y = a + d * dx, b + d * dy
            if not (0 <= x - 1 < len(grid) and 0 <= y - 1 < len(grid[0]) and grid[x - 1][y - 1] == '#'):
                return False
    for dx, dy in directions:
        x, y = a + (n + 1) * dx, b + (n + 1) * dy
        if 0 <= x - 1 < len(grid) and 0 <= y - 1 < len(grid[0]) and grid[x - 1][y - 1] == '.':
            return True
    return False


if __name__ == "__main__":
    main()
