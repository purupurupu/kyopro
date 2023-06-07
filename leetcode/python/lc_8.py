from concurrent.futures.thread import BrokenThreadPool
import re
from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = s
        bfstr = False
        neg_flag = False
        prev_flag = False
        count = 0
        i = 0

        if len(s) == 0:
            return 0

        while count < len(s):
            if prev_flag == True and len(s) == 1:
                return 0

            if res[0] == "+":
                if prev_flag == True:
                    return 0

                prev_flag = True
                res = res[1:]
                i -= 1

            elif res[0] == "-":
                if prev_flag == True:
                    return 0

                prev_flag = True
                neg_flag = True
                res = res[1:]
                i -= 1

            elif res[0] == "0":
                res = res[1:]
                i -= 1

            elif len(re.findall(r"[a-z]", s[count])) == 1 or len(re.findall(r"[, .!?]", s[count])):
                res = res[:i]
                i -= 1
                bfstr = True
                break

            else:
                i += 1
                count += 1
                prev_flag = False

            if i == 0 and bfstr == True:
                return 0

        if prev_flag == True:
            return 0

        if neg_flag:
            if int("-" + res) < -(2**31):
                return -2147483648
            else:
                return int("-" + res)
        else:
            if len(res) == 0:
                return 0
            if int(res) > (2**31)-1:
                return 2147483648-1
            return int(res)


n = "42"
n = "   -42"
n = "4193 with words"
n = "words and 987"
# n = "-91283472332"
# n = "3.14159"
# n = "+÷-12"
# n = "-+12"
# n = ""
n = "+"
n = "00000-42a1234"


tmp = Solution()
out1 = tmp.myAtoi(n)
print(out1)
