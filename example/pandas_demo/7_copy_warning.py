from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 只选出1月的用于分析
    condition = df["ymd"].str.startswith("2018-01")
    # 链式操作其实是多个步骤, 先get 再 set, get后的可能是view也可能是copy, 会有警告
    # df[condition]["wencha"] = df["bWendu"]-df["yWendu"]
    df.loc[condition, "wencha"] = df["bWendu"] - df["yWendu"]
    log.info("head: \n{}".format(df.head()))
    # 方法二
    copy = df[condition].copy()
    copy["wencha"] = df["bWendu"] - df["yWendu"]
    log.info("copy: \n{}".format(copy.head()))
