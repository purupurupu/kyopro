def min_cut(N, M, edges):
    def find_group(x):
        if group[x] == x:
            return x
        else:
            group[x] = find_group(group[x])
            return group[x]

    group = [i for i in range(N + 1)]
    cut_edge = []
    for i in range(M):
        edge = edges[i]
        u = edge[0]
        v = edge[1]
        gu = find_group(u)
        gv = find_group(v)
        if gu == gv:
            cut_edge.append(edge)
        else:
            group[gu] = gv
    return len(cut_edge)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
tmp = min_cut(N, M, edges)

print(tmp)
