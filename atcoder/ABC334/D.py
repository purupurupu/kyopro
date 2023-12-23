def max_sleds(N, Q, reindeers, queries):
    # Sort the reindeer requirements in ascending order
    reindeers.sort()
    
    cumulative_sum = [0]
    for i in range(N):
        cumulative_sum.append(cumulative_sum[-1] + reindeers[i])

    # Function to find maximum number of sleds that can be pulled
    def find_max_sleds(X):
        # Binary search to find the maximum number of sleds
        low, high = 0, N
        while low < high:
            mid = (low + high + 1) // 2
            if cumulative_sum[mid] <= X:
                low = mid
            else:
                high = mid - 1
        return low

    answers = [find_max_sleds(X) for X in queries]
    return answers

N,Q = map(int, input().split()) 
R = list(map(int, input().split()))

# Qの回数分標準入力を受け取る
query = []
for _ in range(Q):
    query.append(int(input()))

res = (max_sleds(N, Q, R, query))

# res の要素を順番に出力する
for i in range(Q):
    print(res[i])