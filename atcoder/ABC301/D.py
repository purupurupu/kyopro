def solve(S, N):
    S = list(S)[::-1]

    L = len(S)

    max_num = 0

    for i in range(L):
        if S[i] == '?':
            if max_num + (1 << i) <= N:
                S[i] = '1'
                max_num += (1 << i)
            else:
                S[i] = '0'
        elif S[i] == '1':
            max_num += (1 << i)

    if max_num > N:
        return -1
    else:
        return max_num


S = input().strip()
N = int(input().strip())

print(solve(S, N))
