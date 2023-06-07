H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]


for s in range(H):
    for t in range(W):
        if all(A[(i + s) % H][(j + t) % W] == B[i][j] for i in range(H) for j in range(W)):
            print("Yes")
            exit()

print("No")
