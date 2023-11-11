import time

# 如果不传值的话就是默认为当前时间戳
now_time = time.localtime()
print(now_time)

second_time = time.localtime(1152528855)
print(second_time)

time_cuo = time.mktime(now_time)
print(time_cuo)

time_str = time.strftime("%Y-%m-%d", now_time)
print(time_str)

date = "2020-05-02  12:03:30"
time_yuanzu = time.strptime(date, "%Y-%m-%d  %H:%M:%S")
print(time_yuanzu)

# 等待10秒钟再运行下面一个代码
time.sleep(10)
