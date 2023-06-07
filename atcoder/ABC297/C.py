H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if S[i][j] == "T" and S[i][j+1] == "T":
            S[i] = S[i][:j] + "P" + "C" + S[i][j+2:]

for s in S:
    print(s)
