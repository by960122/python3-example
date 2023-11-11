# 最长回文子串
# 给你一个字符串 s,找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案
class Sulution5:
    def longestPalindrome(self, content: str) -> str:
        contentLen = len(content)
        # 特殊处理
        if contentLen == 1:
            return content
        # 创建动态规划dynamic programing表
        dp = [[False for _ in range(contentLen)] for _ in range(contentLen)]
        # 初始长度为1,这样万一不存在回文,就返回第一个值（初始条件设置的时候一定要考虑输出）
        max_len = 1
        start = 0
        end = 0
        for rightIndex in range(1, contentLen):
            for leftIndex in range(rightIndex):
                if (content[leftIndex] == content[rightIndex]) and (
                        rightIndex - leftIndex < 3 or dp[leftIndex + 1][rightIndex - 1]):
                    dp[leftIndex][rightIndex] = True
                    if (rightIndex - leftIndex + 1 > max_len):
                        max_len = rightIndex - leftIndex + 1;
                        start = leftIndex;
                        end = rightIndex;
        return content[start:end + 1]
