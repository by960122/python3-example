# N 字形变换
# 将一个给定字符串 s 根据给定的行数 numRows ,以从上往下、从左到右进行Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING"行数为 3 时,排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后,你的输出需要从左往右逐行读取,产生出一个新的字符串,比如："PAHNAPLSIIGYIR"。
# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"

class Solution6:
    def convert(self, content: str, rows: int) -> str:
        if rows < 2: return content
        resultList = ["" for _ in range(rows)]
        currentRow, flag = 0, -1
        for c in content:
            resultList[currentRow] += c
            if currentRow == 0 or currentRow == rows - 1: flag = -flag
            currentRow += flag
        return "".join(resultList)
