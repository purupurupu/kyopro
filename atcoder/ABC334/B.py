A, M, L,R = map(int, input().split())  # 3個の数字の入力を受け取る
first_tree = A + -((A - L) // M) * M if L < A else A + ((L - A + M - 1) // M) * M

last_tree = A + -((A - R) // M) * M if R < A else A + ((R - A) // M) * M

# 範囲内のツリーの総数を計算する
if first_tree > R or last_tree < L:
    res = 0  # 範囲外の場合は0を返す
else:
    res = (last_tree - first_tree) // M + 1

print(res)