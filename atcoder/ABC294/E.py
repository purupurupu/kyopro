N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(1, N + 1):
    k = i - 1
    possible = 0
    for j in range(1, N + 1):
        if (k - (j - 1)) % 2 == 0 and 1 <= k - (j - 1) * (A[j - 1] - 1) <= j:
            possible += 1
    if possible == 1:
        ans += 1

print(ans)
