S= input()

char_count = {}

for char in S:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_char = min(char_count, key=lambda k: (-char_count[k], k))

print(max_char)