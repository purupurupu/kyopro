import bisect

n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for i in range(n):
    j = bisect.bisect_left(a, a[i]+x)
    if j < n and a[j] == a[i]+x:
        print("Yes")
        exit()

print("No")
