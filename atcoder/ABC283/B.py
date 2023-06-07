import sys

N = int(input())
A = list(map(int, input().split()))  # n個の数字がリストに格納される

Q = int(input())

# print(N)
# print(A)
# print(Q)


for i in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    pattern = len(query)

    if pattern == 2:
        print(A[query[1]-1])

    if pattern == 3:
        A[query[1]-1] = query[2]
        # print(A[query[1]-1])

sys.exit()
