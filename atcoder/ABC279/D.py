import math

A, B = map(int, input().split())

bf_time = A
time = 0

for i in range(1, 1000000000000000000):
    time = (B * i-1) + (A / math.sqrt(i))

    if bf_time >= time:
        bf_time = time

    elif time > bf_time:
        break

print(format(bf_time, '.10f'))
