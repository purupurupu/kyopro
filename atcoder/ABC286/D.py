import sys

n, x = map(int, input().split())
coins = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (x + 1)
dp[0] = 1
for coin in coins:
    for i in range(x, coin[0] - 1, -1):
        for j in range(1, coin[1] + 1):
            if i - j * coin[0] >= 0 and dp[i - j * coin[0]]:
                dp[i] = 1
if dp[x]:
    print("Yes")
else:
    print("No")
