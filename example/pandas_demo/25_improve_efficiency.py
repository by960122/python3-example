from example.pandas_demo import log, pd

if __name__ == '__main__':
    # Pandas 的 Categorical 数据类型可以降低数据存储提升计算速度: 将全部的字符串存储 -> 变成数字中间存储, 大幅降低存储空间
    df_users = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/users.dat",
                           sep=":",
                           engine="python",
                           names="UserID:Gender:Age:Occupation:Zip-core".split(":"))

    log.info("df_users: \n{}".format(df_users.head()))
    # info 方法不用打印就能在控制台输出
    log.info("df_users info: ")
    df_users.info()
    log.info("df_users info deep: ")
    df_users.info(memory_usage="deep")
    df_users_copy = df_users.copy()
    df_users_copy["Gender"] = df_users_copy["Gender"].astype("category")
    log.info("df_users_copy value_counts: \n{}".format(df_users_copy["Gender"].value_counts()))
    # 内存量会降低
    log.info("df_users_copy info deep: ")
    df_users_copy.info(memory_usage="deep")
    # 也能提升运算速度
    # df_users.groupby("Gender").size()
    # df_users_copy.groupby("Gender").size()
