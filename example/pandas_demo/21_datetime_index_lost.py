import matplotlib.pyplot as plt

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # 缺失索引填充
    # dataFrame.reindex, 调整dataframe的索引I以适应新的索引
    # dataFrame.resample, 可以对时间序列重采样, 支持补充缺失值
    df = pd.DataFrame({"pdate": ["2019-12-01", "2019-12-02", "2019-12-04", "2019-12-05"], "pv": [100, 200, 400, 500],
                       "uv": [10, 20, 40, 50]})
    log.info("index init: {}".format(df.index))
    # 问题现象: 没有12-03 的横坐标, 但图是连续的, 这种其实不明显, 按理说图应该中断
    # df = df.set_index("pdate")
    # 将pdate设置为索引的同时,转为日期格式, 注意观察dtype 由 object > datetime64,
    # 特别注意: 后边的reindex生成的 datetime64 类型, 若没有这一步, 会匹配不到数据
    df = df.set_index(pd.to_datetime(df["pdate"])).drop("pdate", axis=1)
    log.info("index set: {}".format(df.index))
    # 1. reindex: 生成完整的日期序列,值按0填充
    # df = df.reindex(pd.date_range(start="2019-12-01", end="2019-12-05"), fill_value=0)
    # log.info("reindex: {}".format(df.index))
    # 2. resample: 改变数据的时间频率,比如把天数据变成月份,或者把小时数据变成分钟级别
    # 特别注意: 此处不加 fillna(0) 有断片的效果, 上面要么没断片效果, 要么没横坐标, 其实都不如这种直观
    df = df.resample("D").mean().fillna(0)
    log.info("head: \n{}".format(df.head()))
    df.plot()
    plt.show(block=True)
