# 経路を表すグラフ
graph = [[] for _ in range(N)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# 検証済みの閉路の数
closed_count = 0

# DFSでグラフのすべての閉路を検出する


def dfs(u, prev):
    for v in graph[u]:
        if v == prev:
            continue
        dfs(v, u)
        closed_count += 1


# 閉路を検出する
dfs(0, -1)

# 閉路の数を最小の削除辺数とする
ans = closed_count
print(ans)
