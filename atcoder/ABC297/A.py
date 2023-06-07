# import sys
# import copy

# n, d = map(int, input().split())  # 3個の数字の入力を受け取る
# t_list = list(map(int, input().split()))  # n個の数字がリストに格納される

n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = -1
for i in range(n):
    for j in range(i+1, n):
        if t[j] - t[i] <= d:
            if ans == -1:
                ans = t[j]
            else:
                ans = min(ans, t[j])
            break

print(ans)
