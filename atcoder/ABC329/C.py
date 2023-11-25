def count_consecutive_chars(s):
    max_counts = {}
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            if s[i - 1] not in max_counts or current_count > max_counts[s[i - 1]]:
                max_counts[s[i - 1]] = current_count
            current_count = 1

    if s[-1] not in max_counts or current_count > max_counts[s[-1]]:
        max_counts[s[-1]] = current_count

    total_count = sum(max_counts.values())

    return total_count

n = int(input())
s = input()

res = count_consecutive_chars(s)

print(res)
