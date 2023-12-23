from collections import deque

def min_operations(N, edges):
    # 隣接リストの作成
    adj = [[] for _ in range(N + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # BFSで各頂点までの距離を求める
    dist = [-1] * (N + 1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        v = queue.popleft()
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)

    # 最大距離を求める
    return max(dist)

# 入力例1
print(min_operations(9, [(1, 2), (2, 3), (2, 4), (2, 5), (1, 6), (6, 7), (7, 8), (7, 9)]))  # 出力例1: 5

# 入力例2
print(min_operations(6, [(1, 2), (2, 3), (2, 4), (3, 5), (3, 6)]))  # 出力例2: 1

# 入力例3
print(min_operations(24, [(3, 6), (7, 17), (7, 20), (7, 11), (14, 18), (17, 21), (6, 19), (5, 22), (9, 24),
                          (11, 14), (6, 23), (8, 17), (9, 12), (4, 17), (2, 15), (1, 17), (3, 9), (10, 16),
                          (7, 13), (2, 16), (1, 16), (5, 7), (1, 3)]))  # 出力例3: 12
