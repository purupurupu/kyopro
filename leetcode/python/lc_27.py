

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for _ in range(nums.count(val)):
            nums.remove(val)

        return nums


nums = [3, 2, 2, 3]
val = 3

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

tmp = Solution()
out1 = tmp.removeElement(nums, val)
print(out1)
