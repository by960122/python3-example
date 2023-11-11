# 无重复字符的最长子串
# 给定一个字符串 s ,请你找出其中不含有重复字符的最长子串的长度。
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc",所以其长度为 3
class Solution3:
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        # 哈希集合记录每个字符是否出现过
        characters = set()
        # 右指针初始值为 -1相当于我们在字符串的左边界的左侧还没有开始移动
        rightIndex, ans = -1, 0
        for leftIndex in range(len(s)):
            if leftIndex != 0:
                # 左指针向右移动一格移除一个字符
                characters.remove(s[leftIndex - 1])
            while rightIndex + 1 < len(s) and s[rightIndex + 1] not in characters:
                # 不断地移动右指针
                characters.add(s[rightIndex + 1])
                rightIndex += 1
            # 第 leftIndex 到 rightIndex 个字符是一个极长的无重复字符子串
            ans = max(ans, rightIndex - leftIndex + 1)
        return ans
