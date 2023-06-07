from typing import List, Optional
import copy


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        loopFlag = False
        i, j = 0, 0

        if m == 0:
            for i in range(n):
                nums1.append(nums2[i])
                if i == n-1:
                    nums1.pop(0)
                return nums1

        for val2 in nums2:
            # for i, val1 in enumerate(range(m+n)):
            loopFlag = False

            while loopFlag == False:
                if nums1[i] >= val2:
                    # upperIndex = j
                    nums1.insert(i, val2)
                    nums1.remove(0)
                    loopFlag = True

                elif nums1[i+1] == 0:
                    # nums1[i] = val2
                    nums1.insert(i+1, val2)
                    nums1.remove(0)
                    loopFlag = True
                i += 1
        return nums1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1

tmp = Solution()

out1 = tmp.merge(nums1, m, nums2, n)

print(out1)
