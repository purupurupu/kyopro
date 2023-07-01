# N = int(input())
# success_rates = []
# for i in range(N):
#     Ai, Bi = map(int, input().split())
#     success_rate = Ai / (Ai + Bi)
#     success_rates.append((success_rate, i+1))

# success_rates.sort(key=lambda x: (-x[0], x[1]))

# for _, i in success_rates:
#     print(i, end=' ')

N = int(input())
people = []
for i in range(N):
    Ai, Bi = map(int, input().split())
    people.append((Ai, Bi, i+1))

people.sort(key=lambda x: (-x[0]/(x[0]+x[1]), x[2]))

for _, _, i in people:
    print(i, end=' ')
