def find_steps(a, b):
    count = 0
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        count += 1
    return count


a, b = map(int, input().split())
result = find_steps(a, b)
print(result)
