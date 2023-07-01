# def solve(N, A, S):
#     # Initialize variables
#     cnt = [0]*3
#     ans = 0
#     cur = 0
#     zero = 0

#     # Reverse order to calculate
#     for i in range(N)[::-1]:
#         if S[i] == 'M':
#             ans += cnt[0]*zero
#         if S[i] == 'E':
#             cnt[0] += zero
#         if S[i] == 'X':
#             zero += 1
#         cnt[A[i]] += 1
#         while cur < 3 and cnt[cur] > 0:  # Add condition `cur < 3`
#             cur += 1

#     # return answer
#     return ans


# N = int(input())
# A = list(map(int, input().split()))
# S = input()

# print(solve(N, A, S))

import sys


def main():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    S = sys.stdin.readline().strip()

    cnt = [0, 0, 0]  # Count of each number before 'M'
    cnt_after_e = [0, 0, 0]  # Count of each number after 'E' and before 'X'
    sum_ = 0  # Total sum
    m_pos, e_pos = -1, -1  # Positions of 'M' and 'E'

    for i in range(N):
        if S[i] == 'M':
            m_pos = i
            cnt[A[i]] += 1
        elif S[i] == 'E':
            if m_pos != -1:
                e_pos = i
                cnt_after_e = cnt.copy()  # Copy count of each number
        elif S[i] == 'X' and e_pos != -1:
            # The first number that doesn't exist in cnt_after_e is the mex
            mex = cnt_after_e.index(0)
            sum_ += mex
            cnt_after_e[A[i]] += 1

    print(sum_)


main()
