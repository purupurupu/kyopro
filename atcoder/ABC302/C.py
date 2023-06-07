from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]


def diff_by_one(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1


for perm in permutations(S):
    if all(diff_by_one(s1, s2) for s1, s2 in zip(perm, perm[1:])):
        print("Yes")
        break
else:
    print("No")
