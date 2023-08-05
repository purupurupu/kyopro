def solve(N, A):
    total = sum(A)
    avg, rem = divmod(total, N)

    count = sum(a - avg - (i < rem)
                for i, a in enumerate(sorted(A, reverse=True)) if a > avg + (i < rem))
    return count


N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))
