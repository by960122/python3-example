from pandas_demo import log, pd

if __name__ == '__main__':
    # 分层索引: 在一个轴向上拥有多个索引层级, 可以表达更高维度数据的形式
    # 可以更方便的进行数据筛选, 如果有序则性能更好
    # roupby等操作的结果, 如果是多KEY, 结果是分层索引, 需要会使用
    # 一般不需要自己创建分层索引, 它有构造函数, 一般不用
    file_path = "C:/WorkSpace/python3-example/material/股票.xlsx"
    df = pd.read_excel(file_path)
    log.info("unique: \n{}".format(df["公司"].unique()))
    # 1. Series 的分层索引 MultiIndex
    df_mean = df.groupby(["公司", "日期"])["收盘"].mean()
    log.info("df_mean: \n{}".format(df_mean))
    log.info("df_mean type: {}".format(type(df_mean)))
    log.info("index: \n{}".format(df_mean.index))
    # 1.1 筛选数据
    log.info("loc: \n{}".format(df_mean.loc["BIDU"]))
    log.info("loc: {}".format(df_mean.loc["BIDU", "2019-10-02"]))
    # 通用. 把二级索引变成列
    log.info("unstack: \n{}".format(df_mean.unstack()))
    # 通用. 把索引变成普通的列
    log.info("reset_index: \n{}".format(df_mean.reset_index()))
    # 2. DataFrame 的 Series
    log.info("df: \n{}".format(df.head()))
    df.set_index(["公司", "日期"], inplace=True)
    log.info("df set_index: \n{}".format(df.head()))
    df.sort_index(inplace=True)
    log.info("df sort_index: \n{}".format(df.head()))
    # 2.1 筛选数据:
    # 元组(key1,key2)代表筛选多层索引, 其中key1是索引引第一级, key2是第级比key1=JD,key2=2019-10-02
    # 列表[key1, key2]代表同一层的多个KEY, 其中key1和key2是并列的同级索引, 比如key1=JD, key2=BIDU
    log.info("df: \n{}".format(df.loc["BIDU"]))
    log.info("df: \n{}".format(df.loc[("BIDU", "2019-10-02"), :]))
    log.info("df: \n{}".format(df.loc[("BIDU", "2019-10-02"), "开盘"]))
    log.info("df: \n{}".format(df.loc[["BIDU", "JD"], "开盘"]))
    log.info("df: \n{}".format(df.loc[(["BIDU", "JD"], "2019-10-03"), :]))
    log.info("df: \n{}".format(df.loc[(["BIDU", "JD"], "2019-10-03"), "收盘"]))
    log.info("df: \n{}".format(df.loc[("BIDU", ["2019-10-02", "2019-10-03"]), "收盘"]))
    # slice 代表筛选这一列的所有内容
    log.info("df: \n{}".format(df.loc[(slice(None), ["2019-10-02", "2019-10-03"]), "收盘"]))
