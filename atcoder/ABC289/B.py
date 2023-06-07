import sys


N, M = map(int, input().split())
num_list = list(map(int, input().split()))

tmp_list = []
n_list = list(range(1, N+1))
res = []

if M == 0:
    for i in n_list:
        print(i, end=" ")
    sys.exit()


def extract_sequences(lst):
    result = []
    sub_list = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] == 1:
            sub_list.append(lst[i])
        else:
            result.append(sub_list)
            sub_list = [lst[i]]
    result.append(sub_list)
    return result

# print(extract_sequences([1, 3, 4, 5, 6, 8, 9, 10]))


extract_list = extract_sequences(num_list)
# print(extract_list)

for i, l in enumerate(extract_list):
    n_list[l[0]-1:l[-1]+1] = reversed(n_list[l[0]-1:l[-1]+1])
    # print(n_list)

for i in n_list:
    print(i, end=" ")
