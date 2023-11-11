#  示例 1：
#
#  输入：x = 121
#  输出：true
#  示例2：
#
#  输入：x = -121
#  输出：false
#  解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#  示例 3：
#
#  输入：x = 10
#  输出：false
#  解释：从右向左读, 为 01 。因此它不是一个回文数。
#
#  如果反转后的数字大于 int.MAX,我们将遇到整数溢出问题。
#
#  按照第二个想法,为了避免数字反转可能导致的溢出问题,为什么不考虑只反转 int 数字的一半？毕竟,如果该数字是回文,其后半部分反转后应该与原始数字的前半部分相同
#
#  所有负数都不可能是回文
#  所有个位是 0 的数字不可能是回文

class Solution9:
    def isPalindrome(self, inputNumber: int) -> bool:
        if inputNumber < 0 or (inputNumber % 10 == 0 and inputNumber != 0):
            return False
        revertedNumber = 0
        while inputNumber > revertedNumber:
            revertedNumber = revertedNumber * 10 + inputNumber % 10
            inputNumber //= 10
        return inputNumber == revertedNumber or inputNumber == revertedNumber // 10

    # 字符写法
    def isPalindrome(self, inputNumber: int) -> bool:
        return inputNumber >= 0 and (s := str(inputNumber)) == s[::-1]
