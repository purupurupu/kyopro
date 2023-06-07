def resolve(S, T):
    # if len(S) != len(T):
    #     return "No"

    # cheat_count = 0
    # for s, t in zip(S, T):
    #     if s == t:
    #         continue
    #     if (s == "@" and t in "atcoder") or (t == "@" and s in "atcoder"):
    #         continue
    #     cheat_count += 1

    # if cheat_count == 0:
    #     return "Yes"
    # else:
    #     return "No"
    replaceable_chars = ['a', 't', 'c', 'o', 'd', 'e', 'r']

    for s, t in zip(S, T):
        if s != t:
            if s == "@":
                if t not in replaceable_chars:
                    return "No"
            elif t == "@":
                if s not in replaceable_chars:
                    return "No"
            else:
                return "No"
    return "Yes"


S = input()
T = input()

result = resolve(S, T)

print(result)
