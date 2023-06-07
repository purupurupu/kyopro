n, m = map(int, input().split())

if m == 0:
    if n <= 1:
        print("Yes")
    else:
        print("No")
else:
    degrees = [0] * n

    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        degrees[u] += 1
        degrees[v] += 1

    two_degree_count = 0
    for i in range(n):
        if degrees[i] == 2:
            two_degree_count += 1
        elif degrees[i] != 1:
            print("No")
            break
    else:
        if two_degree_count == n-2:
            print("Yes")
        else:
            print("No")
