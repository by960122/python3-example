import matplotlib.pyplot as plt

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # 环比(month-to-month): 相邻
    # 同比(year-to-year): 同期
    file_path = "C:/WorkSpace/python3-example/material/beijing_tianqi.csv"
    df = pd.read_csv(file_path, index_col="ymd", parse_dates=True)
    # 如果发现 index 没有变成 DatetimeIndex, 可能时日期格式不对, 下面这种写法会报具体的错误
    # df["ymd"] = pd.to_datetime(df["ymd"])
    # df.set_index("ymd", inplace=True)
    log.info("df index: {}".format(df.index))
    df["bWendu"] = df["bWendu"].str.replace("C", "").astype(int)
    df["yWendu"] = df["yWendu"].str.replace("C", "").astype("int64")
    df = df[["bWendu"]].resample("ME").mean()
    df.sort_index(ascending=True, inplace=True)
    # log.info("df: \n{}".format(df.head()))
    # log.info("df index: {}".format(df.index))
    df.plot()
    plt.show(block=True)
    # 方法1: pct_change, 它直接算好了 (新-旧)/旧 的百分比
    df["bWendu_way1_huanbi"] = df["bWendu"].pct_change(periods=1, fill_method=None)
    df["bWendu_way1_tongbi"] = df["bWendu"].pct_change(periods=12, fill_method=None)
    # 方法2: shift, 用于移动数据, 但保持索引不变
    df_shift_1 = df["bWendu"].shift(periods=1)
    df_shift_12 = df["bWendu"].shift(periods=12)
    df_shift = pd.concat([df["bWendu"], df_shift_1, df_shift_12], axis=1)
    log.info("df_shift: \n{}".format(df_shift.head()))
    df["bWendu_way2_huanbi"] = (df["bWendu"] - df_shift_1) / df_shift_1
    df["bWendu_way2_tongbi"] = (df["bWendu"] - df_shift_12) / df_shift_12
    # 方法3: diff, 用于新值 - 旧值, 跨越N个单位的减法
    df_diff_1 = df["bWendu"].diff(periods=1)
    df_diff_12 = df["bWendu"].diff(periods=12)
    df["bWendu_way3_huanbi"] = df_diff_1 / (df["bWendu"] - df_diff_1)
    df["bWendu_way3_tongbi"] = df_diff_12 / (df["bWendu"] - df_diff_12)
    log.info("df: \n{}".format(df.head()))
