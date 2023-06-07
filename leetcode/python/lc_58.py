

from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res = 0

        # for i in range(len(s)):
        #     if i == 0:
        #         continue
        #     if i == len(s)-1:
        #         break

        #     if s[i] == " " and s[i-1].isalnum and s[i+1].isalnum:
        #         res = i

        # return res
        res = 0
        count = 0
        spaceFlag = False
        countInFalse = 0

        for v in s:

            if v == " ":
                spaceFlag = True
                if count > res:
                    res = count
                    count = 0
                count = 0

            elif v.isalnum() == True and spaceFlag == True:
                count += 1
                res = count

            elif spaceFlag == False:
                countInFalse += 1

        if spaceFlag == False and res == 0:
            return countInFalse

        elif spaceFlag == True and res == 0:
            return countInFalse

        if res == 0:
            return count

        return res


s = "Hello World"
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
# s = "H "
# s = "Today is a nice day"

tmp = Solution()
out1 = tmp.lengthOfLastWord(s)
print(out1)
