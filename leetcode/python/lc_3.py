class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length = 0
        # max_length = 0
        # for i in range(len(s)):
        #     if max_length < length:
        #         max_length = length
        #     stack = []

        #     for j, x in enumerate(s[i:], i):
        #         if j == 0:
        #             stack.append(x)
        #             if len(s) == 1:
        #                 max_length = len(s)

        #             continue

        #         if stack.count(x) > 0:
        #             length = len(stack)
        #             if max_length < length:
        #                 max_length = length
        #             stack = []

        #         stack.append(x)
        #         length = len(stack)

        # return max_length

        start = maxLength = 0
        usedChar = {}
        for index, char in enumerate(s):
            # 重複が発生したらstartを重複発生地点にする。
            # 重複した地点より以降に出現した文字列であればスタート再設置
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                # 重複が発生するまで、maxLengthは更新されていくような動き。
                maxLength = max(maxLength, index - start + 1)
            usedChar[char] = index
        return maxLength


# input = "abcabcbb"
input = "abcabcdbb"

input = "tmmzuxt"
# input = "asjrgapa"
# input = "au"


tmp = Solution()
res = tmp.lengthOfLongestSubstring(input)

print(res)
