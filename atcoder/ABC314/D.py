def solve(N, S, Q, operations):
    for i in range(Q):
        t, x, c = operations[i]

        # Modify a specific character
        if t == 1:
            S = S[:x-1] + c + S[x:]

        # Convert all uppercase characters to lowercase
        elif t == 2:
            S = S.lower()

        # Convert all lowercase characters to uppercase
        elif t == 3:
            S = S.upper()

    return S


N = int(input().strip())
S = input().strip()

# Input for Q and operations
Q = int(input().strip())
operations = []
for _ in range(Q):
    data = input().strip().split()
    t = int(data[0])
    x = int(data[1])
    c = data[2]
    operations.append((t, x, c))

result = solve(N, S, Q, operations)

print(result)
