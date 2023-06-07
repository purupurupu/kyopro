import heapq
from collections import defaultdict, deque

# 入力
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# グラフの構築
G = defaultdict(list)
for u, v in edges:
    G[u-1].append(v-1)  # 0-indexedにする
    G[v-1].append(u-1)

# 各頂点の次数を数える
degree = [len(G[i]) for i in range(N)]

# 中心の候補となる頂点とその次数を集める（次数が大きい順に取り出すため、-degで格納）
centers = [(-deg, i) for i, deg in enumerate(degree) if deg > 1]
heapq.heapify(centers)  # ヒープ化

stars = []
while centers:
    deg, center = heapq.heappop(centers)  # 次数最大の頂点（星の中心）を取り出す
    stars.append(-deg - 1)  # 中心同士をつなぐエッジを除いたものがレベル
    for v in G[center]:  # 取り出した中心に隣接する頂点（他の中心）の次数を更新
        if degree[v] > 1:  # まだ中心として存在する場合
            degree[v] -= 1
            centers.remove((-degree[v] - 1, v))  # 次数を更新するため古い情報を削除
            heapq.heapify(centers)  # ヒープを再構成
            centers.append((-degree[v], v))  # 更新後の次数で追加
            heapq.heapify(centers)  # ヒープを再構成

# 昇順にソートして出力
stars.sort()
print(*stars)
