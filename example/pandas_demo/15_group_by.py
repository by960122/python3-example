import matplotlib.pyplot as plt
import numpy as np

from pandas_demo import log, pd

if __name__ == '__main__':
    df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
                       "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
                       "C": np.random.randn(8),
                       "D": np.random.randn(8)})
    log.info("df: \n{}".format(df.head(10)))
    log.info("group sum: \n{}".format(df.groupby("A").sum()))
    # A,B 会变成二级索引
    log.info("group mean: \n{}".format(df.groupby(["A", "B"]).mean()))
    log.info("group mean as_index: \n{}".format(df.groupby(["A", "B"], as_index=False).mean()))
    # 同时查看多种数据统计
    log.info("group agg: \n{}".format(df.groupby("A")[["C", "D"]].aggregate(["sum", "mean", "std"])))
    # 不同列使用不同的聚合函数
    log.info("group agg: \n{}".format(df.groupby("A")[["C", "D"]].aggregate({"C": ["sum", "std"], "D": "mean"})))
    # 返回的时按名称的多个group对象
    for name, group in df.groupby("A"):
        log.info("name: {}".format(name))
        log.info("group: \n{}".format(group))
    # 可以获取单个分组的数据
    log.info("get_group: \n{}".format(df.groupby("A").get_group("bar")))

    # 案例
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    df["month"] = df["ymd"].str[:7]
    # 每月的最高温度
    df_max_wendu = df.groupby("month")["bWendu"].max()
    log.info("group max: \n{}".format(df_max_wendu))
    # plot 需要依赖 matplotlib mplid3, 注意在 pycharm 设置(Tools -> Python plots)不要开 use interactive model, 有区别注意观察
    log.info("plot: \n{}".format(df_max_wendu.plot()))
    # plt.show(block=True)
    # 每个月的最高温度, 最低温度, 平均空气质量指数
    df_aggregate = df.groupby("month").aggregate({"bWendu": "max", "yWendu": "min", "aqi": "mean"})
    log.info("plot: \n{}".format(df_aggregate.plot()))
    # 这行放在 plot 后边
    plt.show(block=True)
