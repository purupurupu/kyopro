MOD = 998244353

# 入力を受け取る
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

# 隣り合う2枚のカードに書かれた数が同じでないように裏返し方を数え上げる
# dp[i][0]: i番目のカードを表向きにする場合の数
# dp[i][1]: i番目のカードを裏向きにする場合の数
dp = [[0]*2 for _ in range(N+1)]
dp[1][0] = dp[1][1] = 1

for i in range(2, N+1):
    a, b = AB[i-1][0], AB[i-1][1]
    if a != AB[i-2][0] and b != AB[i-2][1]:
        # i番目のカードを表向きにする場合は、i-1番目のカードは裏向き
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
        # i番目のカードを裏向きにする場合は、i-1番目のカードは表向き
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
    else:
        # i番目のカードを表向きにする場合は、i-1番目のカードは裏向き
        dp[i][0] = dp[i-1][1]
        # i番目のカードを裏向きにする場合は、i-1番目のカードは表向き
        dp[i][1] = dp[i-1][0]

# 全てのカードが表向きの場合と、1枚以上裏向きの場合を足して答えを出力する
ans = (dp[N][0] + dp[N][1]) % MOD
print(ans)
