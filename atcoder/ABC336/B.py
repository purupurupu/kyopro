N = int(input())

# Nを2進数に変換
N_bin = bin(N)[2:]

# N_binの末尾から連続する0の数を数える
count = 0
for i in range(len(N_bin)):
    if N_bin[-(i + 1)] == '0':
        count += 1
    else:
        break

print(count)