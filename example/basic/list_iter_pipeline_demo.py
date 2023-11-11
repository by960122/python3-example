import bz2
import fnmatch
import gzip
import os
import re
from collections.abc import Iterable


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence. 
    yield from 语句, 它将 yield 操作代理到父生成器上去, 详细例子参见: flatten 方法
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)


# 如果将来的时候你想扩展管道, 你甚至可以在生成器表达式中包装数据. 比如, 下面这个版本计算出传输的字节数并计算其总和
# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
# bytes = (int(x) for x in bytecolumn if x != '-')
# print('Total', sum(bytes))

# 总结: 
# itertools.chain() 函数同样有类似的功能, 但是它需要将所有可迭代对象作为参数传入. 在上面这个例子中, 你可能会写类似这样的语句 lines = itertools.chain(*files) , 这将导致 gen_opener() 生成器被提前全部消费掉
# 但由于 gen_opener() 生成器每次生成一个打开过的文件,  等到下一个迭代步骤时文件就关闭了, 因此 chain() 在这里不能这样使用. 上面的方案可以避免这种情况。

# isinstance(x, Iterable) 检查某个元素是否是可迭代的. 如果是的话, yield from 就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了
# 额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符. 这样的话字符串数组就能最终返回我们所期望的结果了
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            # 如果不 yield from, 要用 for 循环代替
            # for i in flatten(x):
            #     yield i
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
print('list flatten from digit:', list(flatten(items)))
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
print('list flatten from str:', list(flatten(items)))
