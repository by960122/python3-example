from example.pandas_demo import log, pd

if __name__ == '__main__':
    # 拼接excel列, 类似于 MySQL 关联表后取出两张表的字段
    df_score = pd.read_excel("C:/WorkSpace/python3-example/material/学生成绩表.xlsx")
    df_info = pd.read_excel("C:/WorkSpace/python3-example/material/学生信息表.xlsx")
    log.info("df_score: \n{}".format(df_score.head()))
    log.info("df_info: \n{}".format(df_info.head()))
    # 取出要拼接的列
    df_info = df_info[["学号", "姓名", "性别"]]
    df_merge = pd.merge(left=df_score, right=df_info, left_on="学号", right_on="学号")
    log.info("df_merge: \n{}".format(df_merge.head()))
    log.info("df_merge columns: {}".format(df_merge.columns))
    new_columns = df_merge.columns.to_list()
    log.info("new_columns: {} - {}".format(new_columns, type(new_columns)))
    # 倒叙遍历, 插入到学号后边
    for name in ["姓名", "性别"][::-1]:
        new_columns.remove(name)
        new_columns.insert(new_columns.index("学号") + 1, name)

    df_merge = df_merge.reindex(columns=new_columns)
    log.info("df_merge finished: \n{}".format(df_merge.head()))
    # df_merge.to_excel("C:/WorkSpace/python3-example/material/学生成绩-信息表.xlsx",index=False)
