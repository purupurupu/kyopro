def solve(N, S, operations):
    # Keep track of the characters that need to be changed and their changed values
    changes = {}

    # Use a single variable to manage the conversion state.
    # 0: No change, 1: Convert to lower, 2: Convert to upper
    conversion_state = 0

    for t, x, c in operations:
        if t == 1:
            changes[x] = c
        elif t == 2:
            if conversion_state == 2:
                conversion_state = 0
            else:
                conversion_state = 1
        elif t == 3:
            if conversion_state == 1:
                conversion_state = 0
            else:
                conversion_state = 2

    # Convert the string based on the final conversion_state
    if conversion_state == 1:
        S = S.lower()
    elif conversion_state == 2:
        S = S.upper()

    # Apply the changes recorded in the changes dictionary
    for idx, char in changes.items():
        S = S[:idx-1] + char + S[idx:]

    return S


N = int(input().strip())
S = input().strip()

Q = int(input().strip())
operations = []
for _ in range(Q):
    data = input().strip().split()
    t = int(data[0])
    x = int(data[1])
    c = data[2]
    operations.append((t, x, c))

result = solve(N, S, operations)

print(result)
