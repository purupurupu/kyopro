N,K = map(int, input().split())  # 3個の数字の入力を受け取る
A = list(map(int, input().split()))  # n個の数字がリストに格納される


def calculate_min_oddness(N, K, missing_colors):
    missing_colors.sort()

    oddness = 0
    pairs_to_make = (2 * N - K) // 2

    if K == 0 or K == 1:
        return 0

    # Calculate oddness for pairs between missing socks
    for i in range(1, K):
        oddness += missing_colors[i] - missing_colors[i - 1] - 1

    oddness += missing_colors[0] - 1  # Start
    oddness += N - missing_colors[-1] # End

    if (2 * N - K) % 2 == 1:
        gaps = [missing_colors[i] - missing_colors[i - 1] - 1 for i in range(1, K)]
        gaps.append(missing_colors[0] - 1)
        gaps.append(N - missing_colors[-1])
        oddness -= max(gaps)

    return oddness

print(calculate_min_oddness(N, K, A))