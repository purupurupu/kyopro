N = int(input())

S = list(map(int, input().split()))

A = []

for i in range(N):
    if i == 0:
        A.append(S[0])
    else:
        A.append(S[i] - S[i-1])

for i in A:
    print(i, end=" ")
