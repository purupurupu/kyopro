N = int(input())
S = input()

x, y = 0, 0
record = {(x, y)}

for i in range(N):
    if S[i] == 'R':
        x += 1
    elif S[i] == 'L':
        x -= 1
    elif S[i] == 'U':
        y += 1
    else:
        y -= 1
    record.add((x, y))

if len(record) == N+1:
    print('No')
else:
    print('Yes')
