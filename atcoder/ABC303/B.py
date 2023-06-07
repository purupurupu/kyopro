N, M = map(int, input().split())
a_list = []
for _ in range(M):
    a = list(map(int, input().split()))
    a_list.append(a)

count = 0
for i in range(N):
    for j in range(i + 1, N):
        is_unfriendly = True
        for k in range(M):
            if abs(a_list[k].index(i + 1) - a_list[k].index(j + 1)) == 1:
                is_unfriendly = False
                break
        if is_unfriendly:
            count += 1

print(count)
