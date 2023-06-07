from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = [[]]
        res = [[] for i in range(numRows)]

        for i in range(numRows):
            if i == 0:
                res[i].append(1)
            elif i == 1:
                res[i].append(1)
                res[i].append(1)
            else:
                res[i].append(1)

                for j in range(i-1):
                    tmp = res[i-1][j] + res[i-1][j+1]
                    res[i].append(tmp)

                res[i].append(1)

        # print(res)

        return res


numRows = 5
# numRows = 1
tmp = Solution()

out1 = tmp.generate(numRows)

print(out1)
