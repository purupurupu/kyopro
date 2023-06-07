N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
D = D**2  # prepare for comparing with squared distance

infected = [0]*N
infected[0] = 1
infected_people = [0]

while infected_people:
    new_infected = []
    for i in infected_people:
        Xi, Yi = XY[i]
        for j in range(N):
            if not infected[j]:
                Xj, Yj = XY[j]
                if (Xi-Xj)**2 + (Yi-Yj)**2 <= D:
                    infected[j] = 1
                    new_infected.append(j)
    infected_people = new_infected

for i in infected:
    if i:
        print("Yes")
    else:
        print("No")
