S = [input() for _ in range(8)]

row = col = -1
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            row = i
            col = j
            break
    if row != -1:
        break

# print(row, col)

if (row == 0):
    row = "8"
elif (row == 1):
    row = "7"
elif (row == 2):
    row = "6"
elif (row == 3):
    row = "5"
elif (row == 4):
    row = "4"
elif (row == 5):
    row = "3"
elif (row == 6):
    row = "2"
elif (row == 7):
    row = "1"

if (col == 0):
    col = "a"
elif (col == 1):
    col = "b"
elif (col == 2):
    col = "c"
elif (col == 3):
    col = "d"
elif (col == 4):
    col = "e"
elif (col == 5):
    col = "f"
elif (col == 6):
    col = "g"
elif (col == 7):
    col = "h"

print(col + row)
