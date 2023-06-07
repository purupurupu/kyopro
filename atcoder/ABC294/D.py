# def fun(N, M):
#     min_X = None
#     for a in range(1, N + 1):
#         q, r = divmod(M, a)
#         if r != 0:
#             q += 1
#         b = q
#         if b <= N:
#             X = a * b
#             if min_X is None or X < min_X:
#                 min_X = X
#     return min_X if min_X is not None else -1


# N, M = map(int, input().split())
# result = fun(N, M)

# print(result)


# import math


# def func(N, M):
#     ans = float('inf')
#     for a in range(1, int(math.sqrt(N)) + 1):
#         b = math.ceil(M / a)
#         if a * b >= M and b <= N:
#             ans = min(ans, a * b)
#     return ans if ans != float('inf') else -1


# N, M = map(int, input().split())
# result = func(N, M)

# print(result)

# import math


# def func(N, M):
#     ans = float('inf')
#     for a in range(1, int(math.sqrt(M)) + 1):
#         b = math.ceil(M / a)
#         if a * b >= M and b <= N:
#             ans = min(ans, a * b)
#     return ans if ans != float('inf') else -1


# N, M = map(int, input().split())

# result = func(N, M)

# print(result)

import math


def func(N, M):
    ans = float('inf')
    for a in range(1, N + 1):
        b = math.ceil(M / a)
        if a * b >= M and b <= N:
            ans = min(ans, a * b)
        if a >= math.sqrt(M):
            break
    return ans if ans != float('inf') else -1


N, M = map(int, input().split())
result = func(N, M)
print(result)
