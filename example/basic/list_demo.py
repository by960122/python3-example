import heapq
from itertools import compress
from itertools import groupby
from operator import itemgetter

# list 排序
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
print('sorted_by_fname:', sorted(rows, key=itemgetter('fname')))
print('sorted_by_lname_and_fname:', sorted(rows, key=itemgetter('lname', 'fname')))
print('min_by_lname_and_uid:', min(rows, key=itemgetter('uid')))
print('max_lname_and_uid:', max(rows, key=itemgetter('uid')))


# 内置的 sorted() 函数有一个关键字参数 key, 可以传入一个 callable 对象给它, 这个 callable 对象对每个传入的对象返回一个值, 这个值会被 sorted 用来排序这些对象
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


# print(sorted([User(23), User(3), User(99)], key=lambda u: u.user_id))
# 另外一种方式是使用 operator.attrgetter() 来代替 lambda 函数
# sorted([User(23), User(3), User(99)], key=attrgetter('user_id'))
# 支持多个属性, sorted(users, key=attrgetter('last_name', 'first_name'))
# 也支持min/max, min(users, key=attrgetter('user_id'))

# list过滤
print('filter:', list(filter(lambda n: n % 2 == 1, range(10))))

# 对 list 施加函数操作
print('map:', list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# list 切片: index下标从0开始, 左闭又开, 第3个位置表示步长(跳跃取值)
R = list(range(100))
print('[0:3] =', R[0:3])  # == R[:3]
print('[1:3] =', R[1:3])
print('[-3:] =', R[-3:])
print('[10:20] =', R[10:20])
print('[:10:2] =', R[:10:2])
print('[::10] =', R[::10])
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates[0] =', classmates[0])
print('classmates[-1] =', classmates[-1])

# 假定你要从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段
record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:37])
# 内置的 slice() 函数创建了一个切片对象。所有使用切片的地方都可以使用切片对象
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
# 更方便的是, 还可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上
a = slice(5, 50, 2)
s = 'HelloWorld'
a.indices(len(s))  # (5, 10, 2)
# for i in range(*a.indices(len(s))):

# list 遍历
print('list for:', [x * x for x in range(1, 11)])
# 双层for 循环遍历
print('list for repeat:', [m + n for m in 'ABC' for n in 'XYZ'])

# list 过滤:
print('list filter by if:', [x * x for x in range(1, 11) if x % 2 == 0])
# 当你需要用另外一个相关联的序列来过滤某个序列的时候，compress 这个函数是非常有用的
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
print('list filter by compress:', list(compress(addresses, [n > 5 for n in counts])))

# set
s1 = set([1, 1, 2, 2, 3, 3])
s2 = set([2, 3, 4])
# 取交集
print('set &: ', s1 & s2)
# 取并集
print('set |: ', s1 | s2)

# list 提取元素
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print('extract content:', price)

# 提取元素 *号: 专门为解压不确定个数或任意个数元素的可迭代对象而设计
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('extract content:', phone_numbers)

# 从一个集合中获得最大或者最小的 N 个元素列表
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('nlargest: ', heapq.nlargest(3, nums))
print('nsmallest: ', heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# 太大的情况下建议先排序, 堆数据结构最重要的特征是 heap[0] 永远是最小的元素. 并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到
# 该方法会先将第一个元素弹出来, 然后用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N),N 是堆大小）
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# heap = list(nums)
# heapq.heapify(heap)

# list 合并元素: heapq.merge() 需要所有输入序列必须是排过序的, 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测
# 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
print('list merge:', list(heapq.merge(a, b)))


# list 删除元素: 怎样在一个序列上面保持元素顺序的同时消除重复的值
# 如果序列上的值都是 hashable 类型,  那么可以很简单的利用集合或者生成器来解决这个问题
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print('delete dict:', list(dedupe(a)))


# 这个方法仅仅在序列中元素为 hashable 的时候才管用. 如果你想消除元素不可哈希(比如 dict 类型)的序列中重复元素的话,  你需要将上述代码稍微改变一下
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# key参数指定了一个函数, 将序列元素转换成 hashable 类型
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# print('delete dict by key:', list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print('delete dict by key:', list(dedupe(a, key=lambda d: d['x'])))

# 分组
# 一个非常重要的准备步骤是要根据指定的字段将数据排序。 因为 groupby() 仅仅检查连续的元素
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print('date:', date)
    for i in items:
        print('date of items:', i)

# 或者放入一个dict
# from collections import defaultdict
# rows_by_date = defaultdict(list)
# for row in rows:
#     rows_by_date[row['date']].append(row)
