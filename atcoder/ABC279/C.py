import sys

H, W = map(int, input().split())

S = []
T = []

calcS = [""] * W
calcT = [""] * W

tmpString = ""

count = 0

for i in range(H):
    tmpString = input()
    for j in range(W):
        calcS[j] += tmpString[j]

for i in range(H):
    tmpString = input()
    for j in range(W):
        calcT[j] += tmpString[j]

distS = list(set(calcS))
distT = list(set(calcT))

lenS = len(distS)
lenT = len(distT)

if lenS != lenT:
    print("No")
    sys.exit()

for i in range(lenS):
    for j in range(lenT):
        if calcS[i] == calcT[j]:
            count += 1

# print(count)


if count == lenS:
    print("Yes")
else:
    print("No")
