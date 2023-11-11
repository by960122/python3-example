from pandas.core.frame import DataFrame

from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 1. 新增列: 直接新增
    df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]
    log.info("新增列: 直接新增: \n{}".format(df.head(3)))


    # 2. apply 应用一个函数
    def get_wendu_type(df: DataFrame):
        if df["bWendu"] > 33:
            return "高温"
        if df["yWendu"] < -10:
            return "低温"
        return "常温"


    df.loc[:, "wendy_type"] = df.apply(get_wendu_type, axis=1)
    log.info("新增列: apply: \n{}".format(df.head(3)))
    log.info("新增列: 统计: \n{}".format(df["wendy_type"].value_counts()))
    # 3. assign(分配): 支持新增多个列
    df = df.assign(yWendu_huashi=lambda x: x["yWendu"] * 9 / 5 + 32,
                   bWendu_huashi=lambda x: x["bWendu"] * 9 / 5 + 32)
    log.info("新增列: assign: \n{}".format(df.head(3)))
    # 4. 按条件选择分组, 分别赋值
    df["wencha_type"] = ""
    df.loc[df["bWendu"] - df["yWendu"] > 10, "wencha_type"] = "温差大"
    df.loc[df["bWendu"] - df["yWendu"] <= 10, "wencha_type"] = "温差正常"
    log.info("按条件选择分组: 统计: \n{}".format(df["wendy_type"].value_counts()))
