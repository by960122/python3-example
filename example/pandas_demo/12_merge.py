from pandas_demo import log, pd

if __name__ == '__main__':
    # 相当于 MySQL 的 join 语法
    # pd.merge(left,right,how=inner,on=None,left_on=None,right_on=None,f_indx=False,righ_index=False,sort=True,suffixes=(x,),copy=True,indicator=False,validate=None)
    # left,right: 要merge的dataframe或者有name的Series
    # how: join类型, left/right/outer/inner
    # on: join的key, left和right都需要有这个key
    # left_on: left的df或者series的key
    # rght_on: right的df或者seires的key
    # left_index, right_index: 使用index而不是普通的column做join
    # sufixes: 两个元素的后缀, 如果列有重名, 自动添加后缀, 默认是(_x, "y)
    # 文档地址: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
    df_ratings = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/ratings.dat",
                             sep="::",
                             engine="python",
                             names="UserID::MovieID::Rating::Timestamp".split("::"))
    df_users = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/users.dat",
                           sep=":",
                           engine="python",
                           names="UserID:Gender:Age:Occupation:Zip-core".split(":"))
    df_movies = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/movies.dat",
                            sep=",",
                            engine="python",
                            names="MovieID,Title,Genres".split(","))
    log.info("df_ratings: \n{}".format(df_ratings.head()))
    log.info("df_users: \n{}".format(df_users.head()))
    log.info("df_movies: \n{}".format(df_movies.head()))

    df_ratings_users = pd.merge(df_ratings, df_users, left_on="UserID", right_on="UserID", how="inner")
    log.info("df_ratings_users: \n{}".format(df_ratings_users.head()))
    df_ratings_users_movies = pd.merge(df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner")
    log.info("df_ratings_users_movies: \n{}".format(df_ratings_users_movies.head()))
    # -------------
    df_left = pd.DataFrame({"sno": [11, 12, 13, 14], "name": ["name_a", "name_b", "name_c", "name_d"]})
    df_right = pd.DataFrame({"sno": [11, 12, 13, 14], "age": ["21", "22", "23", "24"]})
    # 一对一
    df_left_right = pd.merge(df_left, df_right, on="sno")
    log.info("one-one: \n{}".format(df_left_right.head()))
    # 一对多
    df_right = pd.DataFrame(
        {"sno": [11, 11, 11, 12, 12, 13], "scores": ["语文88", "数学90", "英语75", "语文66", "数学55", "英语29"]})
    df_left_right = pd.merge(df_left, df_right, on="sno")
    log.info("one-many: \n{}".format(df_left_right.head()))
    # 多对多
    df_left = pd.DataFrame({"sno": [11, 11, 12, 12, 12], "爱好": ["篮球", "羽毛球", "乒乓球", "篮球", "足球"]})
    df_left_right = pd.merge(df_left, df_right, on="sno")
    log.info("many-many: \n{}".format(df_left_right.head(10)))
    # 重名情况
    df_left = pd.DataFrame({"key": ["k1", "k2", "k3"], "A": ["A1", "A2", "A3"]})
    df_right = pd.DataFrame({"key": ["k1", "k2", "k3"], "A": ["A11", "A22", "A33"]})
    df_left_right = pd.merge(df_left, df_right, on="key", suffixes=("_left", "_right"))
    log.info("duplication-name: \n{}".format(df_left_right.head(10)))
