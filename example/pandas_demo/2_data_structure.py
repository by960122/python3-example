from pandas_demo import log, pd

if __name__ == '__main__':
    # 1. Series 是一种类似于一维数组的对象,它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引l）组成
    s1 = pd.Series(data=[1, "a", 5.2, 7])
    # 左侧为索引, 右侧为数据
    log.info("s1: \n{}".format(s1))
    # 获取索引
    log.info("index: {}".format(s1.index))
    # 获取数据
    log.info("values: {}".format(s1.values))
    # 1.2. 创建一个指定索引的 Series
    s2 = pd.Series(data=[1, "a", 5.2, 7], index=["d", "b", "a", "c"])
    log.info("s2: \n{}".format(s2))
    log.info("s2.a: {}".format(s2["a"]))
    log.info("s2.a.b: \n{}".format(s2[["a", "b"]]))
    # 1.3. 使用python 字典创建 Series
    sdata = {"0hio": 35000, "Texas": 72000, "0regon": 16000, "Utah": 5000}
    s3 = pd.Series(data=sdata)
    log.info("s3: \n{}".format(s3))
    # DataFrame 是一个表格型的数据结构
    # 2.1 根据多个字典序列创建dataframe
    data = {
        "state": ["a", "b", "c", "d", "e"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9],
    }
    df = pd.DataFrame(data=data)
    log.info("df: \n{}".format(df))
    log.info("df.dtypes: \n{}".format(df.dtypes))
    log.info("df.columns: {}".format(df.columns))
    log.info("df.index: {}".format(df.index))
    # 2.2 查询多列/多行, 结果也是一个 DataFrame
    log.info("df.多列: \n{}".format(df[["year", "pop"]]))
    log.info("df.多行: \n{}".format(df.loc[1:2]))
    log.info("df.一行(类型是 Series): \n{}".format(df.loc[1]))
