N, Q = map(int, input().split())

dic = {}
tmpFlag = False

# t, a, b = map(int, input().split())  # 3個の数字の入力を受け取る

# int_list = [input() for _ in range(Q)]
int_list = [list(input().split()) for _ in range(Q)]

# print(int_list)   # 出力を確認

for i in range(N):
    dic[str(i+1)] = ''


for v in int_list:
    if v[0] == "1":
        if dic[v[1]].find(v[2]) != -1:
            continue
        else:
            dic[v[1]] = dic[v[1]] + v[2]

    if v[0] == "2":
        if dic[v[1]].find(v[2]) != -1:
            dic[v[1]] = dic[v[1]].replace(v[2], '')
        else:
            continue

    if v[0] == "3":
        if dic[v[1]].find(v[2]) != -1:
            if dic[v[2]].find(v[1]) != -1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")


# print(dic)
