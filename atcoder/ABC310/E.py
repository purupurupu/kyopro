def solve(N, S):
    total = 0
    A = [int(c) for c in S]
    for i in range(N):
        value = A[i]
        for j in range(i, N):
            if i != j:
                value = 0 if value == 1 and A[j] == 1 else 1
            total += value
    return total


N = int(input().strip())
S = input().strip()
print(solve(N, S))
