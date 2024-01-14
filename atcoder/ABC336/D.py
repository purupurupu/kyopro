def func(N, A):
    left = [0] * N
    right = [0] * N

    for i in range(N):
        if i == 0:
            left[i] = 1
        else:
            left[i] = min(left[i-1] + 1, A[i])

    for i in range(N-1, -1, -1):
        if i == N - 1:
            right[i] = 1
        else:
            right[i] = min(right[i+1] + 1, A[i])

    max_size = 0
    for i in range(N):
        max_size = max(max_size, min(left[i], right[i]))

    return max_size

N = int(input())
A = list(map(int, input().split()))
print(func(N, A))
