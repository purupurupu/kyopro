def solve(A, B, X):
    HX, WX = len(X), len(X[0])
    HA, WA = len(A), len(A[0])
    HB, WB = len(B), len(B[0])
    maxH, maxW = max(HX, HA + HB), max(WX, WA + WB)
    if sum(row.count('#') for row in A) + sum(row.count('#') for row in B) < sum(row.count('#') for row in X):
        return 'No'

    def overlay(C, D, x, y):
        HC, WC = len(C), len(C[0])
        HD, WD = len(D), len(D[0])
        for i in range(HD):
            for j in range(WD):
                if 0 <= i + x < HC and 0 <= j + y < WC:
                    if D[i][j] == '#':
                        C[i + x][j + y] = '#'
        return C

    for i in range(maxH - HA + 1):
        for j in range(maxW - WA + 1):
            for k in range(maxH - HB + 1):
                for l in range(maxW - WB + 1):
                    C = [['.' for _ in range(maxW)] for _ in range(maxH)]
                    C = overlay(C, A, i, j)
                    C = overlay(C, B, k, l)
                    # Cut out the section of C to match the size of X
                    C_cut = [row[:WX] for row in C[:HX]]

                    if any(C[x][y] == '#' for x in range(HX) for y in range(WX)) and C_cut == X:
                        return 'Yes'
    return 'No'


# 入力を受け取る
HA, WA = map(int, input().split())
A = [list(input()) for _ in range(HA)]
HB, WB = map(int, input().split())
B = [list(input()) for _ in range(HB)]
HX, WX = map(int, input().split())
X = [list(input()) for _ in range(HX)]

# 解決関数を呼び出して結果を出力
print(solve(A, B, X))
