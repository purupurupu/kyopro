S = input()
T = input()
res = -1

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        res = i
        break

if res != -1:
    print(res+1)
else:
    print(len(T))
