a, b = map(int, input().split())

count = a // b
if a % b == 0:
    print(count)
else:
    print(count+1)
