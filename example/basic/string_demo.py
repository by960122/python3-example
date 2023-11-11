import re
import sys
from collections import namedtuple
from fnmatch import fnmatch

import unicodedata

# 1. 按开头或者结尾匹配字符串, startswith/endswith 接收字符串或tuple
print('endswith:', 'spam.txt'.endswith('.txt'))
# filename.startswith(tuple('file:'))
# 查找字符串, re的 findall 也可以, 见下文
text = 'yeah, but no, but yeah, but no, but yeah'
print('find:', text.find('no'))

# 1.1 去除两端不需要的字符: strip() 方法能用于删除开始或结尾的字符. lstrip() 和 rstrip() 分别从左和从右执行删除操作. 默认情况下, 这些方法会去除空白字符, 但是你也可以指定其他字符
print('strip:', ' hello world \n'.strip())
# print('strip:',' hello world \n'.lstrip())
# print('strip:',' hello world \n'.rstrip())
print('lstrip:', '-----hello====='.lstrip('-'))
print('rstrip:', '-----hello====='.rstrip('='))

# 1.2 更强大的清理字符. 注意: str.replace() 方法通常是最快的, 如果你需要执行任何复杂字符对字符的重新映射或者删除操作的话,  translate() 方法会非常的快。
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\n'): None,
    ord('\r'): None  # Deleted
}
a = 'pýtĥöñ\fis\tawesome\r\n'.translate(remap)
print('translate: ', a)

# 使用 dict.fromkeys() 方法构造一个字典, 每个Unicode和音符作为键, 对应的值全部为 None, 使用 unicodedata.normalize() 将原始输入标准化为分解形式字符
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print('translate by unicode:', unicodedata.normalize('NFD', a).translate(cmb_chrs))
# 或者一下子丢弃掉那些字符. 当然, 这种方法仅仅只在最后的目标就是获取到文本对应ACSII表示的时候生效。
print('translate by encode and decode: ', unicodedata.normalize('NFD', a).encode('ascii', 'ignore').decode('ascii'))

# 1.3 字符串对齐
print('ljust: ', 'Hello World'.ljust(20))
print('rjust: ', 'Hello World'.rjust(20, '-'))
print('center: ', 'Hello World'.center(20))
print('format: ', format('Hello World', '>20'))
print('format: ', format('Hello World', '=<20'))
print('format: ', format('Hello World', '*^20s'))
print('format: ', '{:>10s} {:>10s}'.format('Hello', 'World'))

# 1.4 字符串拼接(推荐join): 当我们使用加号(+)操作符去连接大量的字符串的时候是非常低效率的, 因为加号连接会引起内存复制以及垃圾回收操作
# https://python3-cookbook.readthedocs.io/zh-cn/latest/c02/p14_combine_and_concatenate_strings.html
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print('join:', ' '.join(parts))

# 1.5 字符串插入
print('insert string by format:', '{name} has {n} messages.'.format(name='Guido', n=37))


# s.format_map(vars()) vars自动会寻找前文同名的变量. 这2种写法的坏处是参数缺失时, 会报错
# 解决办法是定义一个含有 __missing__ 方法的字典对象
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


# s.format_map(safesub(vars()))
# 抽象成全局方法
# def sub(text):
#     return text.format_map(safesub(sys._getframe(1).f_locals))

# 1.6 以指定的列宽将它们重新格式化
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# print(textwrap.fill(s, 70))
# print(textwrap.fill(s, 40, initial_indent='    ')) # 首行空格
# print(textwrap.fill(s, 40, subsequent_indent='    ')) # 非首行空格
# os.get_terminal_size().columns # 获取当前终端的的大小

# 2. 使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串
# fnmatch 使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式, 如果你对这个区别很在意, 可以使用 fnmatchcase() 来代替
print('fnmatch:', fnmatch('foo.txt', '*.txt'))
# print('fnmatch:', fnmatch('foo.txt', '?oo.txt'))
# print('fnmatch:', fnmatch('Dat45.csv', 'Dat[0-9]*'))

# Unicode字符串, 需要确保所有字符串在底层有相同的表示
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print('unique s1: %s, s2: %s, but s1 == s2? %s' % (s1, s2, s1 == s2))
normalize_s1 = unicodedata.normalize('NFC', s1)
normalize_s2 = unicodedata.normalize('NFC', s2)
print('normalize unique s1: %s, s2: %s, s1 == s2? %s' % (normalize_s1, normalize_s2, normalize_s1 == normalize_s2))
# Python同样支持扩展的标准化形式NFKC和NFKD, 它们在处理某些字符的时候增加了额外的兼容特性
s = '\ufb01'
print('unque s: %s, NFD: %s, NFKD: %s, NFKC: %s' % (
    s, unicodedata.normalize('NFD', s), unicodedata.normalize('NFKD', s), unicodedata.normalize('NFKC', s)))

# 3. 需要将一个字符串分割为多个字段, 但是分隔符(还有周围的空格)并不是固定的, split() 方法只适应于非常简单的字符串分割情形
line = 'asdf fjdk; afed, fjek,asdf, foo'
print('re split: ', re.split(r'[;,\s]\s*', line))
# 括号-捕获分组, 可以使得后面的处理更加简单, 因为可以分别将每个组的内容提取出来
# re.split(r'(;|,|\s)\s*', line)
# re.split(r'(?:,|;|\s)\s*', line) # 非捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
month, day, year = m.groups()
print('month: %s, day: %s, year: %s' % (month, day, year))

# 关于 re 的详细用法
# re.match只匹配字符串的开始,如果字符串开始不符合正则表达式,则匹配失败,函数返回None;而re.search匹配整个字符串,直到找到一个匹配
# re.I	使匹配对大小写不敏感, 全称 re.IGNORECASE
# re.L	做本地化识别（locale-aware）匹配, 全称 re.ASCII
# re.M	多行匹配, 影响 ^ 和 $, 全称: re.MULTILINE
# re.S	让正则表达式中的点(.)匹配包括换行符在内的任意字符, 全称: re.DOTALL
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解, 全称: re.VERBOSE
# re.U	根据Unicode字符集解析字符.这个标志影响 \w, \W, \b, \B, 全称: re.UNICODE
# re.match(pattern, string, flags=0)
print('match by start:', re.match(r'www', 'www.runoob.com').span());  # 在起始位置匹配
print('match by not in start:', re.match(r'com', 'www.runoob.com'));  # 不在起始位置匹配
print("search:", re.search(r'com', 'www.runoob.com', re.M | re.I).group());

# 普通的替换操作: 'year month day'.replace('yeah', 'yep')
# re 替换操作
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串
# repl : 替换的字符串,也可为一个函数
# string : 要被查找替换的原始字符串
# count : 模式匹配后替换的最大次数,默认 0 表示替换所有的匹配
# flags : 编译时用的匹配模式,数字形式
phone = "2004-959-559 # 这是一个电话号码";

# 删除注释
num = re.sub(r"#.*$", "", phone);
print("电话号码 : ", num);

# 移除非数字的内容
num = re.sub(r'\D', "", phone);
print("电话号码 : ", num);

s = 'A23G4HFD567';
pattern = re.compile(r'(?P<value>\d+)');
print('pattern.match: ', pattern.match(s));  # 这样居然不行
print('re.search: ', re.search(r'(?P<value>\d+)', s));
print('pattern.findall: ', pattern.findall(s));  # 查找匹配到的所有子串, 如果只匹配一次的话可以简写 re.findall(r'(?P<value>\d+)', s)

it = re.finditer(r"(?P<value>\d+)", s);  # 返回一个迭代器
for match in it:
    print('re.finditer: ', match.group());


# 当 repl 为一个函数的时候
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'));
    return str(value * 2);


print('re.sub by double func: ', re.sub(r'(?P<value>\d+)', double, s));
# 除了替换后的结果外, 还想知道有多少替换发生了
newtext, nums = re.subn(r'(?P<value>\d+)', double, s)
print('re.subn by double func. newtext: %s, nums: %s' % (newtext, nums));

# 贪婪模式(默认)/非贪婪模式: 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配
print('re 贪婪模式:', re.findall(r'"(.*)"', 'Computer says "no."'))
print('re 贪婪模式:', re.findall(r'"(.*)"', 'Computer says "no." Phone says "yes."'))
print('re 非贪婪模式:', re.findall(r'"(.*?)"', 'Computer says "no." Phone says "yes."'))

# 跨越多行匹配
text = '''
/* this is a
multiline comment */
'''
# (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配, 而不能通过单独捕获或者编号的组)
print('多行匹配1:', re.findall(r'/\*((?:.|\n)*?)\*/', text))
print('多行匹配2:', re.findall(r'/\*(.*?)\*/', text, re.S))

# 一个字符串, 想从左至右将其解析为一个令牌流
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 23 + 42 * 10'):
    print(tok)
