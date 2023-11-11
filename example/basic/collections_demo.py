from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple

# 2. 队列: 不设置大小就是无限大小, 一般用于保留有限历史记录
q = deque(['a', 'b', 'c'], maxlen=4)
q.append('x')
q.appendleft('y')
# q.pop()
# q.popleft()
print('deque append:', q)

# 1. dict
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 1.1 带默认值的 dict: 它会自动初始化每个 key 刚开始对应的值
# 案例: 实现一个键对应多个值的字典
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# 1.2 怎样找出一个序列中出现次数最多的元素呢？
# Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象, 底层一个 Counter 对象就是一个字典,将元素映射到它出现的次数上
# 特别适用于计数场景
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 出现频率最高的3个单词
print('word counts: ', word_counts.most_common(3))
# 如果想手动增加计数 word_counts[word] += 1, 或者 word_counts.update(morewords)
# 更强大的是, 它们可以很容易的跟数学运算操作相结合
# a = Counter(words)
# b = Counter(morewords)
# a + b
# a - b


# 1.3 带顺序的dict: 内部维护着一个根据键插入顺序排序的双向链表, 在迭代或序列化这个字典的时候能够控制元素的顺序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# for key in d:
#     print(key, d[key])
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 1.4 如果你在一个字典上执行普通的数学运算, 你会发现它们仅仅作用于键, 而不是值
print('price_min:', min(prices))  # Returns 'AAPL'
print('price_min:', max(prices))  # Returns 'IBM'
# 进一步获取键信息
print('price_min_key:', min(prices, key=lambda k: prices[k]))  # Returns 'FB'
print('price_max_key:', max(prices, key=lambda k: prices[k]))  # Returns 'AAPL'

# 通过zip, 可以很方便的解决, zip能将键值反过来, 注意: 它创建的是一个只能访问一次的迭代器
print('price_min_key_by_zip:', min(zip(prices.values(), prices.keys())))
print('price_max_key_by_zip:', max(zip(prices.values(), prices.keys())))
print('price_sorted_by_zip:', sorted(zip(prices.values(), prices.keys())))

# 1.5 怎样在两个字典中寻寻找相同点(比如相同的键, 相同的值等等)
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# 可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作
# Find keys in common
repeat_keys = a.keys() & b.keys()
print(type(repeat_keys))
# Find keys in a that are not in b
a.keys() - b.keys()  # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items()  # { ('y', 2) }

# 这些操作也可以用于修改或者过滤字典元素, 比如, 假如你想以现有字典构造一个排除几个指定键的新字典
# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}


# 1.6 构造一个字典,它是另外一个字典的子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 字典推导: 更快
p1 = {key: value for key, value in prices.items() if value > 200}
p2 = {key: value for key, value in prices.items() if key in {'AAPL', 'IBM', 'HPQ', 'MSFT'}}
# p2 = { key:prices[key] for key in prices.keys() & tech_names } 这种要慢大概1.6倍
# 转为 dict
p3 = dict((key, value) for key, value in prices.items() if value > 200)

# 3.7: 命名元组: 有一段通过下标访问列表或者元组中元素的代码,但是这样有时候会使得你的代码难以阅读, 于是你想通过名称来访问元素
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print('namedtuple: ', sub.addr, sub.joined)
# 尽管 namedtuple 的实例看起来像一个普通的类实例,但是它跟元组类型是可交换的,支持所有的普通元组操作,比如索引和解压
# addr, joined = sub
# 注意: 命名元组是不可更改的, 只能赋值给新元组
# 简单地: s = s._replace(shares=75), 复杂的如下:
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


dict_to_stock({'name': 'ACME', 'shares': 100, 'price': 123.45})

# 3.8 多dict 查询,合并
# ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表, 用的还是原来的字典
# 如果出现重复键,那么第一次出现的映射值会被返回, 对于字典的更新或删除操作总是影响的是列表中第一个字典
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print('ChainMap x: ', c['x'])  # Outputs 1 (from a)
print('ChainMap y: ', c['y'])  # Outputs 2 (from b)
print('ChainMap z: ', c['z'])  # Outputs 3 (from a)
# 也可以考虑使用 update() 方法将两个字典合并, 但是它需要你创建一个完全不同的字典对象(或者是破坏现有字典结构), 如果原字典做了更新,这种改变不会反应到新的合并字典中去
merged = dict(b)
merged.update(a)
# merged['x'] 同 ChainMap
# merged['y'] 同 ChainMap
# merged['z'] 同 ChainMap
