def can_win(S, T):
    atcoder = set('atcoder')
    count_s = [0]*26
    count_t = [0]*26
    at_s = at_t = 0
    for s, t in zip(S, T):
        if s == '@':
            at_s += 1
        else:
            count_s[ord(s)-97] += 1
        if t == '@':
            at_t += 1
        else:
            count_t[ord(t)-97] += 1

    for i in range(26):
        char = chr(i+97)
        if char in atcoder:
            min_at = min(at_s, at_t)
            at_s -= min_at
            at_t -= min_at
            count_s[i] += min_at
            count_t[i] += min_at
        if count_s[i] != count_t[i]:
            return 'No'
    if at_s != at_t:
        return 'No'
    return 'Yes'


S = input().strip()
T = input().strip()
print(can_win(S, T))
