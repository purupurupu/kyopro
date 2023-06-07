from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def generate(p, left, right, parens=[]):

#             if left:
#                 generate(p + '(', left-1, right)
#             if right > left:
#                 generate(p + ')', left, right-1)
#             if not right:
#                 parens += p,
#             return parens

#         return generate('', n, n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


n = 3
tmp = Solution()
out1 = tmp.generateParenthesis(n)
print(out1)
