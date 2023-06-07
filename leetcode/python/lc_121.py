from typing import List
import copy


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0

        cp_prices = (list(dict.fromkeys(prices)))

        for i, bf in enumerate(cp_prices):
            for j, af in enumerate(cp_prices[i:], len(cp_prices)-1):
                tmp = af - bf
                if tmp > max_num:
                    max_num = tmp
        return max_num


prices = [7, 1, 5, 3, 6, 4]
# prices = [7,6,4,3,1]
prices = [3, 2, 1]


tmp = Solution()

out1 = tmp.maxProfit(prices)

print(out1)
