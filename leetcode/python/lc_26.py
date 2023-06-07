

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s: str = ""
        ss: str = ""
        res = []
        for v in digits:
            s = s + str(v)
        # print(s)

        i = int(s) + 1
        ss = str(i)

        for v in ss:
            # print(v)
            res.append(v)

        # print(res)
        return res


digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [9]

tmp = Solution()
out1 = tmp.plusOne(digits)
print(out1)
