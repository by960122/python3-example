from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/student.xlsx"
    df = pd.read_excel(file_path, skiprows=2)
    log.info("head: \n{}".format(df.head()))
    # isnull/isna/notnull: 检测是否为空, 可用于 df 和 series
    # dropna: 丢弃, 删除缺失值
    #       axis: 删除行还是列, 0 or index, 1 or columns, default 0
    #       how: 如果等于 any 则任何值为空都删除, 如果等于 all 则所有值为空才删除
    #       inplace: 如果为true则修改当前 df, 否则返回新的 df
    # fillna: 填充空值, 也可以是字典
    # 用法1: df['column_name'] = df['column_name'].fillna(0)
    # 用法2: df.fillna({"column_name": 0}, inplace=True)
    # 也可以: df['column_name'] = df['column_name'].replace(np.nan, 0)
    # 还可以: df['column_name'] = df['column_name'].astype(int, errors='ignore')
    #       value: 用于填充的值
    #       method: ffill == forword fill-使用前1个不为空的值填充, bfill == backword fill-使用后1个不为空的值填充
    #       axis: ...
    #       inplace: ...
    # log.info("isnull: \n{}".format(df.isnull()))
    # log.info("isna: \n{}".format(df["分数"].isna()))
    # log.info("notna: \n{}".format(df["分数"].notna()))
    # 删除全是空的列
    df.dropna(axis=1, how="all", inplace=True)
    df.dropna(axis=0, how="all", inplace=True)
    log.info("dropna: \n{}".format(df.head(10)))
    # 将分数为空的填充为0
    df.fillna({"分数": 0}, inplace=True)
    log.info("fillna: \n{}".format(df.head(10)))
    # 将姓名缺失的值填充
    # df["姓名"] = df["姓名"].ffill()
    df.ffill(inplace=True)
    log.info("ffill: \n{}".format(df.head(10)))
    # 保存
    # df.to_excel("C:/WorkSpace/python3-example/material/student_clean.xlsx",index=False)
