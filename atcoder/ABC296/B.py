H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

res = []
for i in range(H):
    s = ''
    for j in range(W):
        if A[i][j] == 0:
            s += '.'
        else:
            s += chr(ord('A') + A[i][j] - 1)
    res.append(s)

for s in res:
    print(s)
