import sys


def main():
    N, Q = map(int, input().split())
    isolated = [i for i in range(1, N+1)]
    connected = {i: set() for i in range(1, N+1)}

    for _ in range(Q):
        query = list(map(int, sys.stdin.readline().split()))

        if query[0] == 1:
            u, v = query[1], query[2]
            connected[u].add(v)
            connected[v].add(u)
            if u in isolated:
                isolated.remove(u)
            if v in isolated:
                isolated.remove(v)
        else:
            v = query[1]
            for u in connected[v]:
                connected[u].remove(v)
            connected[v].clear()
            if v not in isolated:
                isolated.append(v)

        print(len(isolated))


if __name__ == "__main__":
    main()
