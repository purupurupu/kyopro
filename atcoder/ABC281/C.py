import sys
input = sys.stdin.readline

N, T = map(int, input().split())
A_list = list(map(int, input().split()))
i = 0

T = T % sum(A_list)
for i in range(len(A_list)):
    T -= A_list[i]
    if T <= 0:
        break

T += A_list[i]
print(i+1, T)
