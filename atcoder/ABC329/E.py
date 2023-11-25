def can_transform(N, M, S, T):
    # Generate all possible patterns of T for length M
    possible_patterns = set()
    for i in range(M):
        for j in range(i, M):
            pattern = '#' * i + T[i:j+1] + '#' * (M - j - 1)
            possible_patterns.add(pattern)

    # Check the beginning and end of S for a match with the possible patterns
    if not any(S[:M] == pattern or pattern == '#' * M for pattern in possible_patterns):
        return "No"
    if not any(S[-M:] == pattern or pattern == '#' * M for pattern in possible_patterns):
        return "No"

    # If no disqualifying patterns are found, return "Yes"
    return "Yes"


N, M = map(int, input().split())
S= input()
T= input()

res = can_transform(N, M, S, T)

print(res)