# 整数反转
# 给你一个 32 位的有符号整数 x ,返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ,就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
# 输入：x = 123
# 输出：321
# 示例 2：
# 输入：x = -123
# 输出：-321

class Solution7:
    def reverse(self, content: int):
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        result = 0
        while content != 0:
            # INT_MIN 也是一个负数,不能写成 rev < INT_MIN // 10
            if result < INT_MIN // 10 + 1 or result > INT_MAX // 10:
                return 0
            digit = content % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果,因此这里需要进行特殊判断
            if content < 0 and digit > 0:
                digit -= 10
            content = (content - digit) // 10
            result = result * 10 + digit
        return result


if __name__ == '__main__':
    result = Solution7().reverse(1534236469)
    print(result)
