import os

from pandas_demo import log, pd

if __name__ == '__main__':
    work_dir = "C:/WorkSpace/python3-example/material"
    split_dir = "{}/splits".format(work_dir)
    if not os.path.exists(split_dir):
        os.mkdir(split_dir)
    df_source = pd.read_excel("{}/access_pvuv.xlsx".format(work_dir))
    log.info("df_source: \n{}".format(df_source.head()))
    log.info("shape: {}".format(df_source.shape))
    row_count = df_source.shape[0]
    user_names = ["A", "B", "C"]
    split_size = row_count // len(user_names)
    if row_count % len(user_names) != 0:
        split_size += 1

    for index, user_name in enumerate(user_names):
        begin = index * split_size
        end = begin + split_size
        df_sub = df_source.iloc[begin:end]
        file_path = "{}/splits/access_pvuv_{}_{}.xlsx".format(work_dir, user_name, index)
        log.info("split file: {}".format(file_path))
        # df_sub.to_excel(file_path, index=False)

    # 合并文件
    df_list = []
    for excel_name in os.listdir(split_dir):
        excel_path = "{}/{}".format(split_dir, excel_name)
        log.info("excel_path: {}".format(excel_path))
        user_name = excel_name.replace("access_pvuv_", "").replace(".xlsx", "")[0]
        df_split = pd.read_excel(excel_path)
        df_split["username"] = user_name
        df_list.append(df_split)

    df_merge = pd.concat(df_list)
    log.info("shape: {}".format(df_merge.shape))
    log.info("head: \n{}".format(df_merge.head()))
    log.info("value_counts: \n{}".format(df_merge["username"].value_counts()))
