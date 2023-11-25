N = int(input())

players = []

for i in range(N):
    Ci = int(input())
    Ai = list(map(int, input().split()))
    players.append((i+1, Ci, Ai))

X = int(input())

# Xに賭けた人とその賭けた番号の個数のリストを作成
bet_on_X = [(idx, Ci) for idx, Ci, Ai in players if X in Ai]

# このリストを番号の個数でソート
bet_on_X.sort(key=lambda x: x[1])

# 最小の番号の個数を取得
if bet_on_X:

    min_bet = bet_on_X[0][1]
    res = [idx for idx, Ci in bet_on_X if Ci == min_bet]

    print(len(res))
    print(*res)
else:
    print(0)
