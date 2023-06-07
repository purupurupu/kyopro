

from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        res = bin(sum)

        return res[2:]


a = "11"
b = "1"

a = "1010"
b = "1011"

tmp = Solution()
out1 = tmp.addBinary(a, b)
print(out1)
