import matplotlib.pyplot as plt

from example.pandas_demo import log, pd

if __name__ == '__main__':
    df = pd.read_csv("C:/WorkSpace/python3-example/material/beijing_tianqi.csv")
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 将日期转换为pandas日期后, 设置为索引
    # 文档: https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html
    df.set_index(pd.to_datetime(df["ymd"]), inplace=True)
    log.info("head: \n{}".format(df.head()))
    log.info("index: \n{}".format(df.index))
    # 好处1: 高效查询
    log.info("query single: \n{}".format(df.loc["2018-01-01"].head()))
    log.info("query range: \n{}".format(df.loc["2018-01-01":"2018-01-02"].head()))
    log.info("query pattern: \n{}".format(df.loc["2018-01"].head()))
    # log.info("query pattern: \n{}".format(df.loc["2018"].head()))
    # 好处2: 方便的获取周,月,季度
    log.info("week: \n{}".format(df.index.weekday))
    log.info("month: \n{}".format(df.index.month))
    log.info("quarter: \n{}".format(df.index.quarter))

    log.info("week: \n{}".format(df.groupby(df.index.weekday)["bWendu"].max().plot()))
    plt.show(block=True)
