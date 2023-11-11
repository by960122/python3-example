from pandas.core.frame import DataFrame

from pandas_demo import log, pd

if __name__ == '__main__':
    # 1. df.loc方法, 根据行, 列的标签值查询
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    # 设置索引列
    df.set_index("ymd", inplace=True)
    # 替换掉温度后缀, 以下这种写法并不会生效,还是 object
    df.loc[:, "bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df.loc[:, "yWendu"] = df["yWendu"].str.replace("C", "").astype("int32")
    # 这种赋值是可以的
    # df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    # df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    log.info("df: \n{}".format(df.head(3)))
    log.info("df.index: \n{}".format(df.index))
    log.info("df.dtypes: \n{}".format(df.dtypes))
    # 1.1. 使用单个label值查询数据
    log.info("得到单个值: {}".format(df.loc["2018-01-03", "bWendu"]))
    log.info("得到Series: \n{}".format(df.loc["2018-01-03", ["bWendu", "yWendu"]]))
    # 1.2. 使用值列表批量查询
    log.info("值列表批量查询: {}".format(df.loc[["2018-01-03", "2018-01-04", "2018-01-05"], ["bWendu", "yWendu"]]))
    # 1.3. 使用数值区间进行范围查询
    log.info("范围查询1: \n{}".format(df.loc["2018-01-03": "2018-01-05", "bWendu"]))
    log.info("范围查询2: \n{}".format(df.loc["2018-01-03", "bWendu": "fengxiang"]))
    log.info("范围查询3: \n{}".format(df.loc["2018-01-03": "2018-01-05", "bWendu": "fengxiang"]))
    # 1.4. 使用条件表达式查询
    log.info("条件表达式1: \n{}".format(df.loc[df["yWendu"] < -6, :]))
    log.info("条件表达式2: \n{}".format(
        df.loc[(df["bWendu"] <= 30) & (df["yWendu"] >= 15) & (df["tianqi"] == "晴") & (df["aqiLevel"] == 1), :]))
    # 1.5. 调用函数查询
    log.info("函数查询1: \n{}".format(df.loc[lambda df: (df["bWendu"] <= 30) & (df["yWendu"] >= 15), :]))


    def query_my_date(df: DataFrame):
        return df.index.str.startswith("2018-09") & df["aqiLevel"] == 1


    log.info("函数查询2: \n{}".format(df.loc[query_my_date, :]))
    # 2. df.iloc方法, 根据行, 列的数字位置查询
    # 3. df.where方法
    # 4. df.query方法
