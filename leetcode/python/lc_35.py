

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        beforeFlag = False
        beforeIdx = 0

        if target < nums[0]:
            return 0

        for i, val in enumerate(nums):
            if val < target:
                beforeFlag = True
                beforeIdx = i

            if val == target:
                idx = nums.index(target)
                return idx

            if beforeFlag == True and val > target:
                beforeFlag = False
                beforeIdx = i
                return beforeIdx

        return len(nums)


nums = [1, 3, 5, 6]
target = 5

nums = [1, 3, 5, 6]
target = 2

nums = [1, 3, 5, 6]
target = 7

nums = [1, 3, 5, 6]
target = 0

tmp = Solution()
out1 = tmp.searchInsert(nums, target)
print(out1)
