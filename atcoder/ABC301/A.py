N = int(input())
S = input()

t_count = S.count('T')
a_count = N - t_count

if t_count > a_count:
    print('T')
elif t_count < a_count:
    print('A')
elif t_count == a_count:
    if S[-1] == 'T':
        print('A')
    if S[-1] == 'A':
        print('T')
