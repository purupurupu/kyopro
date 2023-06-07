# import heapq

# N, Q = map(int, input().split())

# not_called = [i for i in range(1, N+1)]
# called = []
# heapq.heapify(not_called)

# for i in range(Q):
#     event = list(map(int, input().split()))

#     if event[0] == 1:
#         x = heapq.heappop(not_called)
#         called.append(x)

#     elif event[0] == 2:
#         x = event[1]
#         called.append(x)

#     else:
#         x = heapq.heappop(called)
#         print(x)

# import heapq

# N, Q = map(int, input().split())

# not_called = [i for i in range(1, N+1)]
# called = []
# heapq.heapify(not_called)

# for i in range(Q):
#     event = list(map(int, input().split()))

#     if event[0] == 1:
#         x = heapq.heappop(not_called)
#         called.append(x)

#     elif event[0] == 2:
#         x = event[1]
#         if x in called:
#             called.remove(x)

#     else:
#         print(min(called))


# import queue

# N, Q = map(int, input().split())

# not_called = queue.Queue()
# for i in range(1, N+1):
#     not_called.put(i)

# called = set()

# for i in range(Q):
#     event = list(map(int, input().split()))

#     if event[0] == 1:
#         x = not_called.get()
#         called.add(x)

#     elif event[0] == 2:
#         x = event[1]
#         if x in called:
#             called.remove(x)

#     else:
#         print(min(called))

import heapq

N, Q = map(int, input().split())

not_called = list(range(1, N+1))
heapq.heapify(not_called)

called = set()

for _ in range(Q):
    event = input().split()
    if event[0] == '1':
        x = heapq.heappop(not_called)
        called.add(x)
    elif event[0] == '2':
        x = int(event[1])
        called.remove(x)
    else:
        x = min(called)
        print(x)
