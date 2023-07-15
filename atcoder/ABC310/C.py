N = int(input().strip())
S = [input().strip() for _ in range(N)]

S = [min(s, s[::-1]) for s in S]

print(len(set(S)))
