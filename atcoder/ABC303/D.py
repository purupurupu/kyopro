X, Y, Z = map(int, input().split())
S = input()

N = len(S)
dp = [[[float('inf')]*2 for _ in range(2)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(2):
        for k in range(2):
            if S[i] == 'A':
                if j == 0:
                    dp[i+1][j][1] = min(dp[i+1][j][1], dp[i][j][k] + Y)
                    dp[i+1][1-j][1] = min(dp[i+1][1-j]
                                            [1], dp[i][j][k] + Z + X)
                else:
                    dp[i+1][j][1] = min(dp[i+1][j][1], dp[i][j][k] + X)
                    dp[i+1][1-j][1] = min(dp[i+1][1-j]
                                            [1], dp[i][j][k] + Z + Y)
            else:
                if j == 0:
                    dp[i+1][j][0] = min(dp[i+1][j][0], dp[i][j][k] + X)
                    dp[i+1][1-j][0] = min(dp[i+1][1-j]
                                            [0], dp[i][j][k] + Z + Y)
                else:
                    dp[i+1][j][0] = min(dp[i+1][j][0], dp[i][j][k] + Y)
                    dp[i+1][1-j][0] = min(dp[i+1][1-j]
                                            [0], dp[i][j][k] + Z + X)
res = min(dp[N][0][0], dp[N][0][1], dp[N][1][0], dp[N][1][1])

print(res)
