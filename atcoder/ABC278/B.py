H, M = map(int, input().split())

strH, strM = str(H), str(M)

swapH = ""
swapM = ""

flag = False

while flag == False:
    strH, strM = str(H), str(M)

    if len(strH) == 1:
        strH = '0' + str(H)

    if len(strM) == 1:
        strM = '0' + str(M)

    swapH = strH[0] + strM[0]
    swapM = strH[1] + strM[1]

    if int(swapH) <= 23 and int(swapM) <= 59:
        flag = True
        print(H, M)

    M += 1
    if M == 60:
        M = 0
        H += 1

    if H == 24:
        H = 0
