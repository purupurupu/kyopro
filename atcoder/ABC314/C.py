# def shift_string(N, M, S, C):
#     S_list = list(S)
#     for i in range(1, M+1):
#         temp = []
#         for j, x in enumerate(C):
#             if x == i:
#                 temp.append(S_list[j])

#         # Perform the cyclic shift
#         temp = [temp[-1]] + temp[:-1]

#         idx = 0
#         for j, x in enumerate(C):
#             if x == i:
#                 S_list[j] = temp[idx]
#                 idx += 1
#     return ''.join(S_list)

def shift_string(N, M, S, C):
    S_list = list(S)

    color_indices = {i: [] for i in range(1, M+1)}
    for idx, color in enumerate(C):
        color_indices[color].append(idx)

    for indices in color_indices.values():
        values = [S_list[i] for i in indices]
        values = [values[-1]] + values[:-1]  # Cyclic shift
        for i, val in zip(indices, values):
            S_list[i] = val

    return ''.join(S_list)


N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

print(shift_string(N, M, S, C))
