N = int(input())

if N == 1:
    print(0)
    exit()
elif N == 2:
    print(2)
    exit()
elif N == 3:
    print(4)
    exit()
elif N == 4:
    print(6)
    exit()
elif N == 5:
    print(8)
    exit()

N = N - 1

# Nを5進数に変換
N_5 = ''

while N > 0:
    N_5 = str(N % 5) + N_5
    N //= 5

# 5進数の各桁を10進数に変換
# 0, 1, 2, 3, 4 -> 0, 2, 4, 6, 8
N_10 = ''
for i in range(len(N_5)):
    if N_5[i] == '0':
        N_10 += '0'
    elif N_5[i] == '1':
        N_10 += '2'
    elif N_5[i] == '2':
        N_10 += '4'
    elif N_5[i] == '3':
        N_10 += '6'
    elif N_5[i] == '4':
        N_10 += '8'

print(N_10)