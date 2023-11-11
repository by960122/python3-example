from pandas.core.frame import DataFrame

from pandas_demo import log, pd


def get_nianyueri(df: DataFrame):
    year, month, day = df["ymd"].split("-")
    return "{}年{}月{}日".format(year, month, day)


if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 文档地址: https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling
    log.info("startswith: \n{}".format(df["ymd"].str.startswith("2018-01")))
    # 每次调用都返回一个新的 Series, 所以要先获取 str 属性
    log.info("slice: \n{}".format(df["ymd"].str.replace("-", "").str.slice(0, 6)))

    df["中文日期"] = df.apply(get_nianyueri, axis=1)
    log.info("head: \n{}".format(df.head()))
    # 这种仅限于 pandas series中, 原生 replace 没有正则替换的功能
    log.info("replace-pattern: \n{}".format(df["中文日期"].str.replace("[年月日]", "", regex=True)))
