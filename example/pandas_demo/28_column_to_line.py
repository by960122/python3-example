from pandas.core.frame import DataFrame

from example.pandas_demo import log, pd


def merge_cols(df: DataFrame):
    # 删除空的列
    df = df[df.notna()]
    # 提取值用于合并
    df_values = df.values
    # 合并后的列表, 每个元素是 Supplier + Supplier PN
    result = []
    # 已知是按两列重复, 就设步长为2 进行遍历, 取出每一对
    for index in range(0, len(df_values), 2):
        result.append(f"{df_values[index]}|{df_values[index + 1]}")
    # 将每对用 # 分割, 返回一个大字符串
    return "#".join(result)


if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/多列转多行.xlsx"
    df = pd.read_excel(file_path)
    # 设置: 显示所有列
    pd.set_option('display.max_columns', None)
    # 设置: 设置宽带
    pd.set_option('display.width', None)
    # 设置: 显示所有行
    pd.set_option('display.max_rows', None)
    log.info("df: \n{}".format(df.head()))
    # 提取待合并的列, 一会儿把它们 drop 掉
    merge_names = list(df.loc[:, "Supplier":].columns.values)
    log.info("drop column list: {}".format(merge_names))
    df["merge"] = df.loc[:, "Supplier":].apply(merge_cols, axis=1)
    # 把多余的列删掉
    df.drop(merge_names, axis=1, inplace=True)
    log.info("df merge: \n{}".format(df.head()))
    # 先将 merge 列变成 list 的形式
    df["merge"] = df["merge"].str.split("#")
    log.info("df merge list: \n{}".format(df.head()))
    # 通过 explode 变成多列
    df_explode = df.explode("merge")
    log.info("df_explode: \n{}".format(df_explode.head()))
    # 将一列变成多列
    df_explode["Supplier"] = df_explode["merge"].str.split("|").str[0]
    df_explode["Supplier PN"] = df_explode["merge"].str.split("|").str[1]
    df_explode.drop("merge", axis=1, inplace=True)
    log.info("df_explode result: \n{}".format(df_explode.head()))
    # df.to_excel("C:/WorkSpace/python3-example/material/多列转多行-结果.xlsx",index=False)
