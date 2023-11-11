from pandas_demo import log, pd

if __name__ == '__main__':
    # 用某种合并方式(inner/outer)
    # 着某个轴向(axis=0/1)
    # 把多个Pandas对象(DataFrame/Series)合并成一个
    # concat语法: pandas.concat(objs, axis=0, join='outer', ignore_index=False)
    # objs: 一个列表, 内容可以是DataFrame或者Series, 可以混合
    # axis: 默认是0代表按行合并, 如果等于1代表按列合并
    # join: 合并的时候索引的对齐方式, 默认是outer, 也可以是inner
    # ignore_index: 是否忽略掉原来的数据索引
    # append语法: DataFrame.append(other,ignore_index=False)
    # append只有按行合并, 没有按列合并, 相当于concat按行的简写形式
    # other: 单个dataframe, series, dict, 或者列表
    # gnore_index: 是否忽略掉原来的数据索引
    # pandas.concat的api文档: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
    # pandas.concat的教程: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    # pandas.append的api文档: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
    df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"], "B": ["BO", "B1", "B2", "B3"], "C": ["c0", "c1", "C2", "C3"],
                        "D": ["DO", "D1", "D2", "D3"], "E": ["EO", "E1", "E2", "E3"]})
    df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"], "B": ["B4", "B5", "B6", "B7"], "C": ["c4", "c5", "C6", "C7"],
                        "D": ["D4", "D5", "D6", "D7"], "F": ["F4", "F5", "F6", "F7"]})
    # 1. 默认的concat, 参数为axis=0(按行合并), join=outer, ignore_index=False
    df_concat = pd.concat([df1, df2])
    log.info("df_concat: \n{}".format(df_concat.head(10)))
    # 1.2 使用 inner 过滤不匹配的列
    df_concat = pd.concat([df1, df2], join="inner", ignore_index=True)
    log.info("df_concat: \n{}".format(df_concat.head(10)))
    # 1.3 按列添加
    s1 = pd.Series(list(range(4)), name="F")
    df_concat = pd.concat([df1, s1], axis=1)
    log.info("df_concat: \n{}".format(df_concat.head(10)))
    # 1.4 添加多列
    s2 = df1.apply(lambda x: x["A"] + "_GG", axis=1)
    s2.name = "G"
    log.info("s2: \n{}".format(s2.head(10)))
    df_concat = pd.concat([df1, s1, s2], axis=1)
    log.info("df_concat_one: \n{}".format(df_concat.head(10)))
    # 1.5 可以指定顺序
    df_concat = pd.concat([s1, df1, s2], axis=1)
    log.info("df_concat_many: \n{}".format(df_concat.head(10)))
    # 1.6 可以只有Series
    df_concat = pd.concat([s1, s2], axis=1)
    log.info("df_concat_series: \n{}".format(df_concat.head(10)))
    # 2. 使用 append 按行合并
    df1 = pd.DataFrame(data=[[1, 2], [3, 4]], columns=list("AB"))
    df2 = pd.DataFrame(data=[[5, 6], [7, 8]], columns=list("AB"))
    df_append = df1._append(df2, ignore_index=True)
    log.info("df_append: \n{}".format(df_append.head(10)))
    # 2.1 逐行添加数据
    df_append = pd.DataFrame(data=None, columns=["A"])
    # 2.1.1 低性能版: 每次要赋值
    for num in range(5):
        df_append = df_append._append({"A": num}, ignore_index=True)
    log.info("df_append: \n{}".format(df_append.head(10)))
    # 2.1.2 高性能版: 直接传列表
    df_append = pd.concat([pd.DataFrame(data=[num], columns=["A"]) for num in range(5)], ignore_index=True)
    log.info("df_append: \n{}".format(df_append.head(10)))
