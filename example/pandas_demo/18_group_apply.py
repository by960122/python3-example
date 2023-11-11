from pandas.core.frame import DataFrame

from pandas_demo import log, pd


def ratings_normal(df: DataFrame):
    min_value = df["Rating"].min()
    max_value = df["Rating"].max()
    df["Rating_normal"] = df["Rating"].apply(lambda x: (x - min_value) / (max_value - min_value))
    return df


def get_wendu_top(df: DataFrame, topn: int):
    return df.sort_values(by="bWendu")[["ymd", "bWendu"]][-topn:]


if __name__ == '__main__':
    # pandas 的 groupby 遵从 split(指的就是groupby本身), apply, combine(由pandas处理) 的顺序执行
    df_ratings = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/ratings.dat",
                             sep="::",
                             engine="python",
                             names="UserID::MovieID::Rating::Timestamp".split("::"))
    # 案例1: 评分归一化
    df_ratings = df_ratings.groupby("UserID").apply(ratings_normal, include_groups=False)
    log.info("df_ratings: \n{}".format(df_ratings.head()))

    df = pd.read_csv("C:/WorkSpace/python3-example/material/beijing_tianqi.csv")
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    df["month"] = df["ymd"].str[:7]
    log.info("df: \n{}".format(df.head()))
    # 案例2: 取每月温度最高的n天
    log.info("df: \n{}".format(df.groupby("month").apply(get_wendu_top, topn=2, include_groups=False).head()))
