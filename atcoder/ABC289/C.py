def solve(n, m, s):
    c = [0] * (n + 1)
    for i in range(m):
        for j in range(s[i][0]):
            c[s[i][j + 1]] += 1
    ans = 1
    for i in range(1, n + 1):
        if c[i] == 0:
            return 0
        ans *= c[i]
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    s = [list(map(int, input().split()))[1:] for i in range(m)]
    print(solve(n, m, s))
