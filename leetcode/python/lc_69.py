

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:

        i = 0
        square = 0

        if x == 0:
            return 0

        # if x == 1:
        #     return 1

        while square < x:

            square = i * i

            if square == x:
                return i

            if square > x:
                return i-1

            i += 1


x = 420

tmp = Solution()
out1 = tmp.mySqrt(x)
print(out1)
