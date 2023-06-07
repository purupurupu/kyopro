
N = int(input())
S = input()

N = len(S)
l = [0] * N
for i in range(1, N):
    j = l[i-1]
    while j > 0 and S[j] != S[i]:
        j = l[j-1]
    if S[j] == S[i]:
        j += 1
    l[i] = j
res = [0] * N
for i in range(N-1):
    for j in range(i + 1, N):
        if S[i:i + l[i]] == S[j:j + l[i]]:
            res[i] = l[i]

print(res)
