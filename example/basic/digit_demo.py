import math
import random
from decimal import Decimal
from fractions import Fraction

import numpy as np

# 1. 对浮点数执行指定精度的舍入运算: round 函数返回离它最近的偶数(四舍五入)
print('round:', round(1.23, 1))
print('round:', round(-1.27, 1))
print('round:', round(1.25361, 3))
# 传给 round() 函数的 ndigits 参数可以是负数, 这种情况下舍入运算会作用在十位、百位、千位等上面
print('round:', round(1627731, -1))
print('round:', round(1627731, -2))
print('round:', round(1627731, -3))

# 2. 需要对浮点数执行精确的计算操作,并且不希望有任何小误差的出现
print('+: ', 4.2 + 2.1)
print('decimal +: ', Decimal(4.2) + Decimal(2.1))
print('sum:', sum([1.23e+18, 1, -1.23e+18]))
print('fsum:', math.fsum([1.23e+18, 1, -1.23e+18]))

# 3. 数字的格式化输出
print('foramt:', format(1234.56789, '0.2f'))
print('foramt by >', format(1234.56789, '>10.1f'))
print('foramt by <', format(1234.56789, '<10.1f'))
print('foramt by ^', format(1234.56789, '^10.1f'))
print('foramt by ,', format(1234.56789, ','))
# 指数计数法
print('foramt:', format(1234.56789, 'e'))
print('foramt:', format(1234.56789, '0.2e'))
# 甚至可以转换输出(地区差异)
print('format and translate:', format(1234.56789, ',').translate({ord('.'): ',', ord(','): '.'}))

# 4. 十进制 > N进制
x = 1234
print('二进制:', bin(x))
print('八进制:', oct(x))
print('十六进制:', hex(x))
print('二进制 format:', format(x, 'b'))
print('八进制 format:', format(-1234, 'o'))
print('十六进制 format:', format(-1234, 'x'))
# format 是带符号输出的,
print('二进制 format 无符号:', format(2 ** 32 + (-1234), 'b'))
print('十六进制 format 无符号:', format(2 ** 32 + (-1234), 'x'))

# 5. N进制转十进制
print('十六进制 -> 十进制:', int('4d2', 16))
print('二进制 -> 十进制:', int('10011010010', 2))
# 特别注意, python 的八进制前缀是 0o, os.chmod('script.py', 0o755)

# 6. 将一个字节字符串并想将它解压成一个整数。或者,你需要将一个大整数转换为一个字节字符串。
# 字节顺序规则(little或big)仅仅指定了构建整数时的字节的低位高位排列方式
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print('byte -> little int:', int.from_bytes(data, 'little'))
print('from -> big int:', int.from_bytes(data, 'big'))
# 反之
# x = 94522842520747284487117727783387188
# print('little int -> byte:',x.to_bytes(16, 'little'))
# print('big int -> byte:',x.to_bytes(16, 'big'))
# 如果是超大整数, 可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值
x = 523 ** 23
nbytes, rem = divmod(x.bit_length(), 8)
if rem: nbytes += 1
print('big int -> byte:', x.to_bytes(nbytes, 'little'))

# 7. 复数
# https://python3-cookbook.readthedocs.io/zh-cn/latest/c03/p06_complex_math.html

# 8. 创建或测试正无穷、负无穷或NaN(非数字)的浮点数
print('正无穷:', float('inf'))
print('负无穷:', float('-inf'))
print('Nan:', float('nan'))
print('判定:', math.isinf(float('inf')))
print('判定:', math.isnan(float('nan')))

# 9. 分数运算
a = Fraction(5, 4)
b = Fraction(7, 16)
print('fraction add:', a + b)
c = a * b
print('分子: %d, 分母: %d' % (c.numerator, c.denominator))
print('float:', float(c))
# 限制分母的情况下, 取最接近的分数
print('limit_denominator:', print(c.limit_denominator(8)))
x = 3.75
print('转分数:', Fraction(*x.as_integer_ratio()))

# 10. 大数据集(比如数组或网格)上面执行计算
# http://www.numpy.org
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print('x * 2: ', x * 2)
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print('ax *: ', ax * 2)
print('ax +: ', ax + 10)
print('ax +: ', ax + ay)
print('ax *: ', ax * ay)


def f(x):
    return 3 * x ** 2 - 2 * x + 7


print('多项式计算:', f(ax))
# 这类要比单纯循环用math更高效, np.sqrt(ax) / np.cos(ax)
# 底层实现中, NumPy 数组使用了C或者Fortran语言的机制分配内存, 也就是说,它们是一个非常大的连续的并由同类型数据组成的内存区域
# 比如,如果你想构造一个10,000*10,000的浮点数二维网格,很轻松. grid = np.zeros(shape=(10000,10000), dtype=float)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('np where:', np.where(a < 10, a, 10))

# 11. 执行矩阵和线性代数运算, 比如矩阵乘法、寻找行列式、求解线性方程组等等
# https://python3-cookbook.readthedocs.io/zh-cn/latest/c03/p10_matrix_and_linear_algebra_calculation.html
# 12. 随机选择
values = [1, 2, 3, 4, 5, 6]
print('random choice:', random.choice(values))
# 为了提取出N个不同元素的样本用来做进一步的操作, 可以使用 random.sample()
print('random sample:', random.sample(values, 2))
# 如果你仅仅只是想打乱序列中元素的顺序, 可以使用 random.shuffle()
print('random shuffle:', random.shuffle(values))
# 生成随机整数, 请使用 random.randint()
print('random randint:', random.randint(0, 10))
# 为了生成0到1范围内均匀分布的浮点数, 使用 random.random()
print('random random:', random.random())
# 如果要获取N位随机位(二进制)的整数, 使用 random.getrandbits()
print('random getrandbits:', random.getrandbits(200))
# random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法, 但是你可以通过 random.seed() 函数修改初始化种子
# random.seed() # Seed based on system time or os.urandom()
# random.seed(12345) # Seed based on integer given
# random.seed(b'bytedata') # Seed based on byte data
