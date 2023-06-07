# 2つの列を連長圧縮する関数
def run_length_encoding(a):
    n = len(a)
    res = []
    i = 0
    while i < n:
        v = a[i]
        j = i + 1
        while j < n and a[j] == v:
            j += 1
        res.append((v, j - i))
        i = j
    return res

# 2つの列を比較して、同じ値を持つものの個数を数える関数


def count_matching_pairs(a, b):
    n1 = len(a)
    n2 = len(b)
    i1 = 0
    i2 = 0
    count = 0
    while i1 < n1 and i2 < n2:
        v1, l1 = a[i1]
        v2, l2 = b[i2]
        if v1 == v2:
            count += l1 * l2
            i1 += 1
            i2 += 1
        elif v1 < v2:
            i1 += 1
        else:
            i2 += 1
    return count


# メイン処理
l = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_run_length = run_length_encoding(a)
b_run_length = run_length_encoding(b)
ans = count_matching_pairs(a_run_length, b_run_length)
print(ans)
