def func(a, b):
    count = 0
    while a != 0 and b != 0:
        if a > b:
            count += a // b
            a %= b
        else:
            count += b // a
            b %= a
    return count - 1


a, b = map(int, input().split())
result = func(a, b)
print(result)
