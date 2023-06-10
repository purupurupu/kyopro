H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

str_list = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            str_list.append((i, j))
min_i = min(i for i, j in str_list)
max_i = max(i for i, j in str_list)
min_j = min(j for i, j in str_list)
max_j = max(j for i, j in str_list)

for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
        if S[i][j] == '.':
            print(i+1, j+1)
            exit(0)
