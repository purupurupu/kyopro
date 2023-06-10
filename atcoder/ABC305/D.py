import bisect


def solve():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    # Create list of sleep times and cumulative sleep time
    sleep_times = [(A[i], A[i + 1]) for i in range(1, len(A), 2)]
    cum_sleep = [0]*(N//2+1)
    for i in range(N//2):
        cum_sleep[i+1] = cum_sleep[i] + (sleep_times[i][1] - sleep_times[i][0])

    Q = int(input().strip())
    queries = [list(map(int, input().strip().split())) for _ in range(Q)]

    for l, r in queries:
        idx1 = bisect.bisect_right(A, l) - 1
        idx2 = bisect.bisect_left(A, r)

        # check if l or r is during a sleep
        l_during_sleep = idx1 % 2 == 1
        r_during_sleep = idx2 % 2 == 0

        # adjust idx1 and idx2 to reference to sleep start times
        if l_during_sleep:
            idx1 -= 1
        if r_during_sleep:
            idx2 += 1

        total_sleep = cum_sleep[idx2//2] - cum_sleep[(idx1+1)//2]

        # Adjust total_sleep for l or r that is during sleep
        if l_during_sleep:
            total_sleep += min(A[idx1+1], r) - l
        if r_during_sleep:
            total_sleep += r - max(A[idx2-1], l)

        print(total_sleep)


if __name__ == "__main__":
    solve()
