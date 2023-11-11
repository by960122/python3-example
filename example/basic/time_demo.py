import calendar
import time
from datetime import date, datetime, timedelta, timezone

from dateutil.relativedelta import relativedelta

# 1. time
now_time = time.localtime()
print('now_time:', now_time)
print('time by sec:', time.localtime(1152528855))
print('time to sec:', time.mktime(now_time))
print('time format:', time.strftime("%Y-%m-%d", now_time))
print('time format', time.strptime('2020-05-02 12:03:30', "%Y-%m-%d %H:%M:%S"))

# 2. datetime:
# 用指定日期时间创建datetime
dt = datetime(2015, 4, 19, 12, 20)
print('datetime: ', dt)
print('datetime -> timestamp:', dt.timestamp())
print('timestamp -> datetime:', datetime.fromtimestamp(dt.timestamp(), tz=timezone.utc))
# 从str读取datetime: strptime() 的性能要比你想象中的差很多， 因为它是使用纯Python实现，并且必须处理所有的系统本地设置, 在已知条件下, 建议 datetime(year,month,day) 这种方式
strptime = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', strptime)
# 把datetime格式化输出:
print('strftime:', strptime.strftime('%a, %b %d %H:%M'))

# 对日期进行加减
now = datetime.now()
print('datetime:', now)
print('datetime today:', datetime.today())
print('datetime + 10 hours:', now + timedelta(hours=10))
print('datetime - 1 day:', now - timedelta(days=1))
print('datetime + days hour:', now + timedelta(days=2, hours=12))
print('datetime + month:', now + relativedelta(months=+4))

# 把时间从UTC+0时区转换为UTC+8
utc_dt = datetime.now(tz=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('datetime UTC+0:00:', utc_dt)
print('datetime UTC+8:00:', utc8_dt)

# 2.1 计算一周中某一天上一次出现的日期，例如上一个周五的日期
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print('datetime by reevious:', get_previous_byday('Tuesday'))
print('datetime by reevious:', get_previous_byday('Sunday', datetime(2012, 12, 21)))


# 先计算出一个对应月份第一天的日期. 一个快速的方法就是使用 date 或 datetime 对象的 replace() 方法简单的将 days 属性设置成1即可
# replace() 方法一个好处就是它会创建和你开始传入对象类型相同的对象。
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1),timedelta(hours=6)):
#     print(d)
