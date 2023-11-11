from pandas_demo import log, pd

if __name__ == '__main__':
    df = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/ratings.dat",
                     sep="::",
                     engine="python",
                     names="UserID::MovieID::Rating::Timestamp".split("::"))
    log.info("df_movies: \n{}".format(df.head()))
    # 记忆: agg(新列名=函数,agg(新列名=(原列名,函数),agg(t"原列名": 函数/列表}), agg函数的两种形式,等号代表"把结果赋值给新列",字典/元组代表"对这个列运用这些函数"
    # 聚合后单列-单指标统计: 每个MovieID的平均评分
    df.groupby("MovieID")["Rating"].mean()
    # 聚合后单列-多指标统计: 每个MoiveID的最高评分,最低评分,平均评分
    df.groupby("MovieID")["Rating"].agg(mean="mean", max="max", min="min")
    df.groupby("MovieID").agg({"Rating": ["mean", "max", "min"]})
    # 聚合后多列-多指标统计: 每个MoiveID的评分人数,最高评分,最低评分,平均评分
    df.groupby("MovieID").agg(rating_mean=("Rating", "mean"), user_count=("UserID", lambda x: x.nunique()))
    df.groupby("MovieID").agg({"Rating": ['mean', 'min', 'max'], "UserID": lambda x: x.nunique()})
    df.groupby("MovieID").apply(lambda x: pd.Series({"min": x["Rating"].min(), "mean": x["Rating"].mean()}),
                                include_groups=False)
