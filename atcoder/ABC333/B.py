S = input()
T = input()

# Sを辞書順にソート
sorted_S = sorted(S)
# Tを辞書順にソート
sorted_T = sorted(T)

def is_same_length(p1, p2, q1, q2):
    distances = {
        ('A', 'B'): 1, ('B', 'C'): 1, ('C', 'D'): 1, ('D', 'E'): 1, ('A', 'E'): 1,
        ('A', 'C'): 2, ('B', 'D'): 2, ('C', 'E'): 2, ('A', 'D'): 2, ('B', 'E'): 2,
        ('A', 'D'): 2, ('B', 'E'): 2, ('A', 'C'): 2, ('B', 'D'): 2, ('C', 'E'): 2
    }

    dist_p = distances.get((p1, p2), 0) if p1 != p2 else 0
    dist_q = distances.get((q1, q2), 0) if q1 != q2 else 0

    return 'Yes' if dist_p == dist_q else 'No'

results = is_same_length(sorted_S[0], sorted_S[1], sorted_T[0], sorted_T[1])

print(results)