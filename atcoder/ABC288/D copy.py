def make_zero(X, K):
    for i in range(len(X)):
        c = -((X[i]+K-1)//K) * K
        for j in range(i, len(X)):
            # for j in range(i, i+K):

            X[j] += c
        if all(x % K == 0 for x in X[i:]):
            return "Yes"
    return "No"


n, k = map(int, input().split())
num_list = list(map(int, input().split()))
q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    tmp_list = num_list[l-1:r].copy()
    print(make_zero(tmp_list, k))
