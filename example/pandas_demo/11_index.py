from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/ratings.csv"
    df = pd.read_csv(file_path)
    # index的用途
    # 1. 更方便的查询
    # 2. 可以获得性能提升, 如果index唯一O(1), 不是唯一O(logN), 完全随机O(N)
    # 是否递增
    log.info("is_monotonic_increasing: {}".format(df.index.is_monotonic_increasing))
    # 是否唯一
    log.info("is_unique: {}".format(df.index.is_unique))
    # 对索引进行排序, 返回一个新的 df
    df.sort_index()
    # 默认会删除索引列, 不删除的话设置 drop=False
    df.set_index("userId", inplace=True, drop=False)
    log.info("head: \n{}".format(df.head()))
    # 使用index 查询
    log.info("index query: \n{}".format(df.loc[5].head()))
    # 条件查询
    log.info("range query: \n{}".format(df.loc[df["userId"] == 5].head()))
    # 3. 自动数据对齐
    s1 = pd.Series([1, 2, 3], index=list("abc"))
    s2 = pd.Series([2, 3, 4], index=list("bcd"))
    log.info("s1: \n{}".format(s1))
    log.info("s2: \n{}".format(s2))
    # b/c 会对齐
    log.info("s1+s2: \n{}".format(s1 + s2))

    # 4. 更强大的数据结构支持
    # Categoricallndex, 基于分类数据的Index, 提升性能
    # ultilndex, 多维索引, 用于groupby多维聚合后结果等
    # atetimelndex, 时间类型索引, 强大的日期和时间的方法支持
