def solve(N, T, M, AB):
    MOD = 10**9 + 7

    # Initialize graph
    conflict = [0]*N
    for a, b in AB:
        a -= 1
        b -= 1
        conflict[a] |= 1 << b
        conflict[b] |= 1 << a

    # Find all valid teams
    team = [0]*(1 << N)
    for S in range(1 << N):
        for i in range(N):
            if (S >> i & 1) and (S & conflict[i]):
                break
        else:
            team[S] = 1

    # Count the number of ways to divide the players into T teams
    dp = [[0]*(T+1) for _ in range(1 << N)]
    dp[0][0] = 1
    for S in range(1 << N):
        for j in range(T):
            if dp[S][j]:
                for T in range(1 << N):
                    if team[T] and not (S & T):
                        dp[S | T][j+1] += dp[S][j]
                        dp[S | T][j+1] %= MOD

    return dp[-1][T]
