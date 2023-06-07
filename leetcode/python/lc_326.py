from typing import List
import copy


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 != 0:
                # print("false")
                return "false"

            n /= 3

            if n == 3:
                return "true"


n = 45

tmp = Solution()

out1 = tmp.isPowerOfThree(n)

print(out1)
