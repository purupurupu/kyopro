N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

max_num = max(P[1:])

res = max(0, max_num - P[0] + 1)

print(res)
