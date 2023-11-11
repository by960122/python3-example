import numpy as np
from pandas.core.frame import DataFrame

from pandas_demo import log, pd


def get_sum_value(df: DataFrame):
    return df["A"] + df["B"] + df["C"] + df["D"]


if __name__ == '__main__':
    df = pd.DataFrame(data=np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])
    log.info("head: \n{}".format(df.head()))
    # axis = 0 or index, 如果是单行操作,指的是某一行, 如果是聚合操作, 指的是跨行
    # axis = 1 or columns, 如果是单行操作,指的是某一列, 如果是聚合操作, 指的是跨列
    # 1. 单行/列操作
    log.info("drop-line: \n{}".format(df.drop(1, axis=0)))
    log.info("drop-column: \n{}".format(df.drop("A", axis=1)))
    # 2. 聚合操作
    # 跨行 == 对每列求平均值
    log.info("mean: \n{}".format(df.mean(axis=0)))
    # 跨列 == 对每行求平均值
    log.info("mean: \n{}".format(df.mean(axis=1)))
    log.info("sum: \n{}".format(df.apply(get_sum_value, axis=1)))
