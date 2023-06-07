N = int(input())

ab_count = [0] * (N+1)
for a in range(1, N+1):
    for b in range(1, N+1):
        if a*b > N:
            break
        ab_count[a*b] += 1

cd_count = [0] * (N+1)
for c in range(1, N+1):
    for d in range(1, N+1):
        if c*d > N:
            break
        cd_count[c*d] += 1

ans = 0
for i in range(1, N+1):
    ans += ab_count[i] * cd_count[N-i]

print(ans)
