class Solution:
    def isValid(self, s: str) -> bool:
        tmpArr = []

        for i, val in enumerate(s):

            if val == ")" and "(" in tmpArr and tmpArr[-1] == "(":
                # tmpArr.remove("(")
                tmpArr.pop(-1)
                continue

            if val == "}" and "{" in tmpArr and tmpArr[-1] == "{":
                # tmpArr.remove("{")
                tmpArr.pop(-1)
                continue

            if val == "]" and "[" in tmpArr and tmpArr[-1] == "[":
                # tmpArr.remove("[")
                tmpArr.pop(-1)
                continue

            tmpArr.append(val)

        if len(tmpArr) > 0:

            return False

        return True


# input = "()"
# input = "()[]{}"
# input = "(}"
# input = "{()()()()}"
input = "[([]])"


tmp = Solution()
out = tmp.isValid(input)
print(out)
