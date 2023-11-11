import io
import os
import sys
import tempfile
from io import BytesIO
from io import StringIO
from tempfile import TemporaryFile, TemporaryDirectory

# 1. StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print('write string io:', f.getvalue())
f = StringIO('水面细风生,\n菱歌慢慢声.\n客亭临小市,\n灯火夜妆明.')
while True:
    s = f.readline()
    if s == '':
        break
    print('read string io:', s.strip())

# 2. BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print('write byte io:', f.getvalue())
data = '人闲桂花落,夜静春山空.月出惊山鸟,时鸣春涧中.'.encode('utf-8')
f = BytesIO(data)
print('read byte io:', f.read())

# 3. 读取/写入文件
# rt 读取
# wt 写入
# xt 文件不存在才可以写入
# at 追加写入
# rd 读取字节
# wb 写入字节
# xb 文件不存在才可以写入字节
# with open('somefile.txt', 'rt', encoding='ascii', errors='ignore') as f:
#     data = f.read()

# with open('somefile.txt', 'wt') as f:
#     print('Hello World!', file=f)

# with open('somefile.bin', 'rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')

# with open('somefile.bin', 'wb') as f:
#     text = 'Hello World'
#     f.write(text.encode('utf-8'))

# 二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入, 而不需要中间转换为自己对象
# 很多对象还允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的内存中去. 比如
# import array
# a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
# with open('data.bin', 'rb') as f:
#     f.readinto(a) # array('i', [1, 2, 3, 4, 0, 0, 0, 0])

# 4. 关于打印/写入文件, 定义end参数, 可以避免换行
print('ACME', 50, 91.5, sep=',', end='!!\n')
# 也可以join, 但join要求类型一致
# print(*row, sep=',')

# 5. 读写一个gzip或bz2格式的压缩文件
# with gzip.open('somefile.gz', 'rt') as f:
#     text = f.read()

# with bz2.open('somefile.bz2', 'rt') as f:
#     text = f.read()
# compresslevel: 压缩级别(默认9), 越小越快
# with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
#     f.write(text)

# with bz2.open('somefile.bz2', 'wt') as f:
#     f.write(text)

# gzip.open() 和 bz2.open() 还有一个很少被知道的特性,  它们可以作用在一个已存在并以二进制模式打开的文件上
# 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上, 比如套接字, 管道和内存中文件等
# f = open('somefile.gz', 'rb')
# with gzip.open(f, 'rt') as g:
#     text = g.read()

# 6. 按固定大小(数据块)读取
# 使用 f.readinto() 时需要注意的是, 你必须检查它的返回值, 也就是实际读取的字节数.
# 如果字节数小于缓冲区大小, 表明数据被截断或者被破坏了(比如你期望每次读取指定数量的字节)

# from functools import partial
# with open('somefile.data', 'rb') as f:
#     records = iter(partial(f.read, 32), b'')
#     for r in records:
#         ...

# 7. 读取数据到一个可变数组中, 使用文件对象的 readinto() 方法
# import os.path
#
# def read_into_buffer(filename):
#     buf = bytearray(os.path.getsize(filename))
#     with open(filename, 'rb') as f:
#         f.readinto(buf)
#     return buf

# 特别注意: memoryview,它可以通过零复制的方式对已存在的缓冲区执行切片操作, 甚至还能修改它的内容
# m1 = memoryview(buf)
# m2[:] = b'WORLD'

# 8. 用内存映射一个二进制文件到一个可变字节数组中, 目的可能是为了随机访问它的内容或者是原地做些修改
# import os
# import mmap
#

# mmap.ACCESS_WRITE 写
# mmap.ACCESS_REA 读
# mmap.ACCESS_COPY 仅在本地修改, 不影响到原始文件
# def memory_map(filename, access=mmap.ACCESS_WRITE):
#     size = os.path.getsize(filename)
#     fd = os.open(filename, os.O_RDWR)
#     return mmap.mmap(fd, size, access=access)

# m = memory_map('data')
# m[0:11] = b'Hello World' # 修改其内容
# m.close()

# 9. 使用路径名来获取文件名, 目录名, 绝对路径等等
path = '/Users/beazley/Data/data.csv'
# print('list dir:', os.listdir('somedir'))
print('base name:', os.path.basename(path))
print('dir name:', os.path.dirname(path))
print('split path:', os.path.splitext(path))
print('contruct path:', os.path.join('tmp', 'data', os.path.basename(path)))
print('expand user path:', os.path.expanduser('~/Data/data.csv'))
print('exist path:', os.path.exists(path))
print('is file:', os.path.isfile('/etc/passwd'))
print('is dir:', os.path.isdir('/etc/passwd'))
print('is link:', os.path.islink('/etc/passwd'))
print('real link path:', os.path.realpath('/usr/local/bin/python3'))


# print('path mata:', os.stat('/path'))
# print('path size:', os.path.getsize('/etc/passwd'))
# print('path modify time:', os.path.getmtime('/etc/passwd'))
# print('path modify time:', time.ctime(os.path.getmtime('/etc/passwd')))


# 10. 当打印未知的文件名时, 使用下面的方法可以避免这样的错误
def bad_filename(filename):
    return repr(filename)[1:-1]


# surrogateescape:
# 这种是Python在绝大部分面向OS的API中所使用的错误处理器, 
# 它能以一种优雅的方式处理由操作系统提供的数据的编码问题.
# 在解码出错时会将出错字节存储到一个很少被使用到的Unicode编码范围内.
# 在编码时将那些隐藏值又还原回原先解码失败的字节序列.
# 它不仅对于OS API非常有用, 也能很容易的处理其他情况下的编码错误.
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


# 用法
# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))

# 11. 在不关闭一个已打开的文件前提下增加或改变它的Unicode编码
# f = io.TextIOWrapper(u, encoding='utf-8')
# text = f.read()

# 先使用 detach() 方法移除掉已存在的文本编码层, 并使用新的编码方式代替
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')

# 12. 在文本模式打开的文件中写入原始的字节数据
# I/O系统以层级结构的形式构建而成。 文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode编码/解码层来创建。 buffer 属性指向对应的底层文件。如果你直接访问它的话就会绕过文本编码/解码层
sys.stdout.buffer.write(b'Hello\n')

# 13. 操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件描述符, 你想将它包装成一个更高层的Python文件对象
# Open a low-level file descriptor
# import os
# fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
# Turn into a proper file
# f = open(fd, 'wt')
# f.write('hello world\n')
# f.close()

# 14. 创建临时文件
# 创建一个匿名的临时文件, 可以使用 tempfile.TemporaryFile, 甚至连目录都没有
# NamedTemporaryFile, 带名字的匿名文件
# 如果不想自动删除文件, 追加参数 delete=False
with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()

# with NamedTemporaryFile('w+t', prefix='mytemp', suffix='.txt', dir='/tmp') as f:
#     print('named temp filename is:', f.name)

# 使用
# f = TemporaryFile('w+t')
# f.close()

# 创建临时目录
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
    ...
# Directory and all contents destroyed

# 或者更简单的
print('mkstemp:', tempfile.mkstemp())
print('mkdtemp:', tempfile.mkdtemp())
print('gettempdir:', tempfile.gettempdir())

# 15. 通过串行端口读写数据，典型场景就是和一些硬件设备打交道(比如一个机器人或传感器)
# pip3 install pySerial
# import serial
#
# ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
#                     baudrate=9600,
#                     bytesize=8,
#                     parity='N',
#                     stopbits=1)

# ser.write(b'G1 X50 Y50\r\n')
# resp = ser.readline()

# 16. 序列化对象为字节流, 保存到文件或数据库
# https://docs.python.org/3/library/pickle.html
# 千万不要对不信任的数据使用pickle.load()。
# pickle在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
# 但是某个坏人如果知道pickle的工作原理，
# 他就可以创建一个恶意的数据导致Python执行随意指定的系统命令。
# 因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用。

# 由于 pickle 是Python特有的并且附着在源码上，所有如果需要长期存储数据的时候不应该选用它
# 例如，如果源码变动了，你所有的存储数据可能会被破坏并且变得不可读取

# import pickle
# f = open('somefile', 'wb')
# # 将一个对象转储为一个字符串
# pickle.dump(data, f)
# # 从字节流中恢复一个对象
# f = open('somefile', 'rb')
# data = pickle.load(f)
# data = pickle.loads(s)

# 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象，比如打开的文件，网络连接，线程，进程，栈帧等等。
# 用户自定义类可以通过提供 __getstate__() 和 __setstate__() 方法来绕过这些限制。
# 如果定义了这两个方法，pickle.dump() 就会调用 __getstate__() 获取序列化的对象。类似的，__setstate__() 在反序列化时被调用
# import time
# import threading
#
# class Countdown:
#     def __init__(self, n):
#         self.n = n
#         self.thr = threading.Thread(target=self.run)
#         self.thr.daemon = True
#         self.thr.start()
#
#     def run(self):
#         while self.n > 0:
#             print('T-minus', self.n)
#             self.n -= 1
#             time.sleep(5)
#
#     def __getstate__(self):
#         return self.n
#
#     def __setstate__(self, n):
#         self.__init__(n)

# c = countdown.Countdown(30)
# f = open('cstate.p', 'wb')
# pickle.dump(c, f)
# f.close()

# 线程又重新恢复了!!!
# f = open('cstate.p', 'rb')
# pickle.load(f)
