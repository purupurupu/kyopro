N, Q = map(int, sys.stdin.readline().split())
called = set()
waiting = []
served = set()

for _ in range(Q):
    event = list(map(int, sys.stdin.readline().split()))
    if event[0] == 1:
        for i in range(1, N + 1):
            if i not in called:
                called.add(i)
                heapq.heappush(waiting, i)
                break
    elif event[0] == 2:
        x = event[1]
        if x not in served:
            served.add(x)
            heapq.heappop(waiting)
    elif event[0] == 3:
        while waiting and waiting[0] in served:
            heapq.heappop(waiting)
        if waiting:
            print(waiting[0])
