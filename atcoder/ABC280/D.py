import math

K = int(input())
i = 1
fac = 1

Flag = False

# math.factorial()

for i in range(1, 2000000):
    fac *= i

    if fac % K == 0:
        print(i)
        Flag = True
        break

if Flag == False:
    print(K)
