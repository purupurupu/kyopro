def max_gift_value(N, M, D, A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    i, j = 0, 0
    max_value = -1
    while i < N and j < M:
        if abs(A[i] - B[j]) <= D:
            max_value = max(max_value, A[i] + B[j])
            i += 1
            j += 1
        elif A[i] > B[j]:
            i += 1
        else:
            j += 1
    return max_value


N, M, D = map(int, input().split())  # 3個の数字の入力を受け取る
A = list(map(int, input().split()))  # n個の数字がリストに格納される
B = list(map(int, input().split()))  # n個の数字がリストに格納される

max_gift_value = max_gift_value(N, M, D, A, B)
print(max_gift_value)
