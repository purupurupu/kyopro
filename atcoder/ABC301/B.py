
def insert_numbers(N, A):
    result = []

    def insert_between(a, b):
        if a < b:
            return list(range(a + 1, b))
        else:
            return list(range(a - 1, b, -1))

    for i in range(N - 1):
        result.append(A[i])
        if abs(A[i] - A[i + 1]) != 1:
            result.extend(insert_between(A[i], A[i + 1]))

    result.append(A[-1])
    return result


N = int(input())
A = list(map(int, input().split()))

result = insert_numbers(N, A)

print(' '.join(map(str, result)))
