N, Q = map(int, input().split())
tmpList = [0] * N

for i in range(Q):
    l, r = map(int, input().split())
    if l == 1:
        tmpList[r-1] += 1
    if l == 2:
        tmpList[r-1] = 2
    if l == 3:
        if tmpList[r-1] == 0 or tmpList[r-1] == 1:
            print("No")
        else:
            print("Yes")
