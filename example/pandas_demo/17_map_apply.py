from pandas_demo import log, pd

if __name__ == '__main__':
    # map: 只用于Series, 实现每个值->值的映射
    # apply: 用于Series实现每个值的处理, 用于Dataframe实现某个轴的Series的处理
    # applymap: 只能用于DataFrame, 用于处理该DataFrame的每个元素, 特别注意 applymap 已标记过期, 推荐用 map
    file_path = "C:/WorkSpace/python3-example/material/股票.xlsx"
    df = pd.read_excel(file_path)
    log.info("unique: \n{}".format(df["公司"].unique()))
    dict_company_names = {
        "bidu": "百度",
        "baba": "阿里巴巴",
        "iq": "爱奇艺",
        "jd": "京东"
    }
    # 1. map 方法一:
    df["公司中文1"] = df["公司"].str.lower().map(dict_company_names)
    # 1.1 map 方法二:
    df["公司中文2"] = df["公司"].map(lambda x: dict_company_names[x.lower()])
    # 2. apply
    df["公司中文3"] = df["公司"].apply(lambda x: dict_company_names[x.lower()])
    df["公司中文4"] = df.apply(lambda x: dict_company_names[x["公司"].lower()], axis=1)
    log.info("df: \n{}".format(df.head()))
    # 3. applymap
    df_sub = df[["收盘", "开盘", "高", "低", "交易量"]]
    log.info("df_sub: \n{}".format(df_sub.head()))
    # 将所有数字取证, 应用与所有函数
    # log.info("applymap: \n{}".format(df_sub.applymap(lambda x: int(x))))
    log.info("applymap: \n{}".format(df_sub.map(lambda x: int(x))))
