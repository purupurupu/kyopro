from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

for i in range(N):
    idx = bisect_left(C, A[i]) + 1
    print(idx, end=" ")
print()

for i in range(M):
    idx = bisect_left(C, B[i])+1
    print(idx, end=" ")
print()
