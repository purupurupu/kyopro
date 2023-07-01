N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

dict = {}
dict['none'] = P[0]
res = 0

for i in range(M):
    dict[D[i]] = P[i+1]

for i in C:
    if i in dict:
        res += dict[i]
    else:
        res += dict['none']

print(res)
