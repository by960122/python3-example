import matplotlib.pyplot as plt

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # explode(爆炸): 将一行拆成多行, 前提是要拆成多行的那一列转成List, 然后应用 explode 方法
    df_movies = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/movies.dat",
                            sep=",",
                            engine="python",
                            names="MovieID,Title,Genres".split(","))
    log.info("df_movies: \n{}".format(df_movies.head()))
    # 将 Genres 按|分割并拆分成多行
    df_movies["Genre"] = df_movies["Genres"].map(lambda x: x.split("|"))
    log.info("df_movies: \n{}".format(df_movies.head()))
    # 取出第0个元素, 有两种方法
    # 先取列, 再取列的第0行
    log.info("Genre: {}".format(df_movies["Genre"][0]))
    # 先取第0行, 再取行的列
    log.info("Genre: {}".format(df_movies.iloc[0]["Genre"]))
    df_movies_explode = df_movies.explode("Genre")
    log.info("df_movies_explode: \n{}".format(df_movies_explode.head()))
    log.info("df_movies_explode genre value_counts: \n{}".format(df_movies_explode["Genre"].value_counts()))
    log.info("df_movies_explode genre value_counts plot: {}".format(df_movies_explode["Genre"].value_counts().plot()))
    # 柱状图(bar)
    log.info("df_movies_explode genre value_counts plot bar: {}".format(
        df_movies_explode["Genre"].value_counts().plot.bar()))
    plt.show(block=True)
