import itertools


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    # 只需要定义一个 __iter__() 方法, 将迭代操作代理到容器内部的对象上去
    def __iter__(self):
        return iter(self._children)

    # 以深度优先方式遍历树形节点的生成器
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    # 定义一个生成器函数, 但是它会调用某个你想暴露给用户使用的外部状态值
    # 一个需要注意的小地方是, 如果你在迭代操作时不使用for循环语句, 那么你得先调用 iter(linehistory) 函数
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器
# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作. 一旦生成器函数返回退出, 迭代终止. 我们在迭代中通常使用的for语句会自动处理这些细节
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def count(n):
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print('node:', ch)

    print('list yield:', list(frange(0, 1, 0.125)))
    # 迭代器和生成器不能使用标准的切片操作, 因为它们的长度事先我们并不知道
    # 函数 islice() 返回一个可以生成指定元素的迭代器, 它通过遍历并丢弃直到切片开始索引位置的所有元素. 然后才开始一个个的返回元素, 并直到切片结束索引位置
    # 要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据.  必须考虑到迭代器是不可逆的这个事实.  所以如果你需要之后再次访问这个迭代器的话, 那你就得先将它里面的数据放入一个列表中
    for x in itertools.islice(count(0), 10, 13):
        print('iter slice: ', x)

    # 另一种丢弃的办法: for line in dropwhile(lambda line: not line.startswith('#'), f):

    # 快捷API: 排列组合, 如果你想得到指定长度的所有排列, 你可以传递一个可选的长度参数 permutations(items, 2)
    items = ['a', 'b', 'c']
    for p in itertools.permutations(items):
        print('permutations:', p)
    # 使用 itertools.combinations() 可得到输入集合中元素的所有的组合
    for p in itertools.combinations(items, 3):
        print('combinations:', p)
    # 在计算组合的时候, 一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取了, 那么接下来就不会再考虑它了). 
    # 而函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次
    for p in itertools.combinations_with_replacement(items, 3):
        print('combinations_with_replacement:', p)

    # 在迭代一个序列的同时跟踪正在被处理的元素索引, 为了按传统行号输出(行号从1开始), 你可以传递一个开始参数, enumerate(items, 1)
    for idx, val in enumerate(items):
        print('items:', idx, val)

    # 想同时迭代多个序列, 每次分别从一个序列中取一个元素
    # zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器, 其中x来自a, y来自b. 一旦其中某个序列到底结尾, 迭代宣告结束. 因此迭代长度跟参数中最短序列长度一致
    # 如果这个不是你想要的效果, 那么还可以使用 itertools.zip_longest() 函数来代替
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    # 在多个对象执行相同的操作, 但是这些对象在不同的容器中, 你希望代码在不失可读性的情况下避免写重复的循环
    # 也可以用a+b, 但这会创建一个新的集合, 有额外开销
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in itertools.chain(a, b):
        print('chain:', x)


    # 用迭代器替换while循环
    # iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记(结尾)值作为输入参数. 当以这种方式使用的时候, 它会创建一个迭代器, 这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止
    # 这种特殊的方法对于一些特定的会被重复调用的函数很有效果, 比如涉及到I/O调用的函数. 举例来讲, 如果你想从套接字或文件中以数据块的方式读取数据, 通常你得要不断重复的执行 read() 或 recv().
    # 并在后面紧跟一个文件结尾测试来决定是否终止。这节中的方案使用一个简单的 iter() 调用就可以将两者结合起来了. 其中 lambda 函数参数是为了创建一个无参的 callable 对象, 并为 recv 或 read() 方法提供了 size 参数。
    def reader(s):
        while True:
            data = s.recv(8192)
            if data == b'':
                break
            process_data(data)


    # 替代写法
    def reader2(s):
        for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
            # pass
            process_data(data)

    # 案例
    # f = open('/etc/passwd')
    # for chunk in iter(lambda: f.read(10), ''):
    #     sys.stdout.write(chunk)
