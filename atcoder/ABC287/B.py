n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]

res = 0

for v in n_list:
    count = m_list.count(v[3:6])
    if count > 0:
        res += 1

print(res)
