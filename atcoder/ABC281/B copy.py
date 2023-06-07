S = input()


if 1 <= len(S) <= 10:
    if S[0].isupper() and 100000 <= int(S[1:7]) <= 999999 and S[7].isupper() and S[-1].isupper():
        print("Yes")
    else:
        print("No")
else:
    print("No")
