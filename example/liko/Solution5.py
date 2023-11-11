# 最长回文子串
# 给你一个字符串 s,找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案
class Sulution5:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        # 特殊处理
        if size == 1:
            return s
        # 创建动态规划dynamic programing表
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 初始长度为1,这样万一不存在回文,就返回第一个值（初始条件设置的时候一定要考虑输出）
        max_len = 1
        start = 0
        end = 0
        for r in range(1, size):
            for l in range(r):
                if (s[l] == s[r]) and (r - l <= 3 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if (r - l + 1 > max_len):
                        max_len = r - l + 1;
                        start = l;
                        end = r;
        return s[start:end + 1]
