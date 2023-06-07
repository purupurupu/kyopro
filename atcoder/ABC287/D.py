S = input()
T = input()

for i in range(len(S)):
    S_ = list(S)
    if S[i] == "?":
        S_[i] = T[i]
    if "".join(S_) == T:
        print("Yes")
    else:
        print("No")
