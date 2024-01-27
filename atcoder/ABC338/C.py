N = int(input())
Q = list(map(int, input().split()))  
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 

max_a = max_b = 10**18

for i in range(N):
    if A[i] > 0:
        max_a = min(max_a, Q[i] // A[i])
    if B[i] > 0:
        max_b = min(max_b, Q[i] // B[i])

res = 0

for a_servings in range(max_a + 1):
    remaining = []
    for i in range(N):
        remaining.append(Q[i] - A[i] * a_servings)

    b_servings = 10**18
    for i in range(N):
        if B[i] > 0:
            b_servings = min(b_servings, remaining[i] // B[i])

    res = max(res, a_servings + b_servings)

print (res)