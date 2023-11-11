# 字符串转换整数 (atoi)
# 请你来实现一个myAtoi(string s)函数,使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）
# 函数myAtoi(string s) 的算法如下:
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号,读取该字符（如果有） 确定最终结果是负数还是正数 如果两者都不存在,则假定结果为正
# 读入下一个字符,直到到达下一个非数字字符或到达输入的结尾字符串的其余部分将被忽略
# 将前面步骤读入的这些数字转换为整数（即,"123" -> 123, "0032" -> 32）如果没有读入数字,则整数为 0 必要时更改符号（从步骤 2 开始）
# 如果整数数超过 32 位有符号整数范围 [−231, 231− 1] ,需要截断这个整数,使其保持在这个范围内具体来说,小于 −231 的整数应该被固定为 −231 ,大于 231− 1 的整数应该被固定为 231− 1
# 返回整数作为最终结果
# 注意:
# 本题中的空白字符只包括空格字符 ' '
# 除前导空格或数字后的其余字符串外,请勿忽略 任何其他字符
# 示例1:
# 输入:s = "42"
# 输出:42
# 解释:加粗的字符串为已经读入的字符,插入符号是当前读取的字符
# 第 1 步:"42"（当前没有读入字符,因为没有前导空格）
#          ^
# 第 2 步:"42"（当前没有读入字符,因为这里不存在 '-' 或者 '+'）
#          ^
# 第 3 步:"42"（读入 "42"）
#            ^
# 解析得到整数 42
# 由于 "42" 在范围 [-231, 231 - 1] 内,最终结果为 42

class Solution8:
    def myAtoi(self, content: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', content.lstrip())), 2 ** 31 - 1), -2 ** 31)

    def myAtoi2(self, content: str) -> int:
        content = content.strip()  # 删除首尾空格
        if not content: return 0  # 字符串为空则直接返回
        result, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if content[0] == '-':
            sign = -1  # 保存负号
        elif content[0] != '+':
            i = 0  # 若无符号位，则需从 i = 0 开始数字拼接
        for c in content[i:]:
            if not '0' <= c <= '9': break  # 遇到非数字的字符则跳出
            if result > bndry or result == bndry and c > '7': return int_max if sign == 1 else int_min  # 数字越界处理
            result = 10 * result + ord(c) - ord('0')  # 数字拼接
        return sign * result


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
