from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path)
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    # 1.汇总类统计
    # 1.1 一下子提取所有数字列统计结果
    log.info("describe: \n{}".format(df.describe()))
    # 1.2 查看单个 Series 的数据
    log.info("mean: {}".format(df["bWendu"].mean()))
    # 1.3 最值
    log.info("max: {}".format(df["bWendu"].max()))
    log.info("min: {}".format(df["bWendu"].min()))
    # 2.1 唯一去重
    log.info("unique: {}".format(df["fengxiang"].unique()))
    log.info("value_counts: {}".format(df["fengxiang"].value_counts()))
    # 3. 相关系数
    # 3.1 协方差: 衡量同向/反向的程度, 为正说明同向, 数值越大程度越高, 为负说明反向, 数值越小程度越高
    log.info("cov: {}".format(df["bWendu"].cov(df["yWendu"])))
    # 3.2 相关系数: 衡量相似程度, 等于1时说明正向相似度最大,等于-1说明反向相似度最大
    log.info("corr: {}".format(df["bWendu"].corr(df["yWendu"])))
