from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 1. Series.sort_values(ascending=True,inplace=True)
    # 返回的是 Series, 记得要赋值
    # df["aqiLevel"].sort_values(ascending=False)
    # df.sort_values(by="aqiLevel", ascending=False)
    log.info("head: \n{}".format(df.head()))
    # 2. Datafram.sort_values(by,ascending=True,inplace=True), by: 字符串或List<字符串>, 单列或多列排序
    df = df.sort_values(by=["aqiInfo", "aqiLevel"], ascending=[False, False])
    log.info("head: \n{}".format(df.head()))
