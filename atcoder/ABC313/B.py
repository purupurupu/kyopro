def resolve(N, M, AB):
    is_strongest = [True]*N

    for a, b in AB:
        is_strongest[b-1] = False

    res = []
    for i in range(N):
        if is_strongest[i]:
            res.append(i+1)
    if len(res) == 1:
        return res[0]
    else:
        return -1


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

print(resolve(N, M, AB))
