from typing import List


class Solution:

    strCount = 0
    index = 0

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        for i, val in enumerate(strs):
            if i == 0:
                strCount = len(val)
                index = i
            # strCount = len(val)
            if len(val) > strCount:
                strCount = len(val)
                index = i
            # print(strCount)
            # print(index)

        targetString = strs[index]
        stringCount = 200
        tmpRes = ""
        res = ""

        for i, val in enumerate(strs):
            endFlag = False

            if (i == index):
                continue

            for j in range(len(val)):
                if targetString[j] == val[j]:
                    res = res + val[j]

                else:
                    endFlag = True

                if endFlag == True:
                    break

            tmpRes = res
            res = ""

        return tmpRes


# input = ["flower", "flow", "flight"]
input = ["aaa", "aa", "aaa"]


tmp = Solution()
res = tmp.longestCommonPrefix(input)

print(res)
