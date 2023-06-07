###### 標準入力一覧 ######
N = int(input())
S = input()

l = 0

for i in range(1, N):
    # print(i)
    for j in range(N):
        if j + i < N:

            if S[j] == S[j+i]:
                break

            if S[j] != S[j+i]:
                l += 1

    print(l)
    l = 0


# for i in range(1, N):
#     # print(i)
#     for j, v in enumerate(S):
#         if j + i >= len(S):
#             break
#         if S[j] == S[j+i]:
#             break

#         if S[j] != S[j+i]:
#             l += 1

#     print(l)
#     l = 0
