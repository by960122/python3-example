import matplotlib.pyplot as plt

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # 数据透视
    # 1. 将列式数据变成二维交叉形式 == 列转行
    # 2. 使用 unstack(把多级索引变成列) 实现透视
    # 3. 使用 pivot 简化透视
    df = pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/ratings.dat",
                     sep="::",
                     engine="python",
                     names="UserID::MovieID::Rating::Timestamp".split("::"))
    # 注意这里有时区问题
    df["pdate"] = pd.to_datetime(df["Timestamp"], unit="s", utc=True).dt.tz_convert('Asia/Shanghai').dt.tz_localize(
        None)
    log.info("df: \n{}".format(df.head()))
    # 按 2 列统计, 然后新增一列 pv == 按用户id求和
    df_group = df.groupby([df["pdate"].dt.month, "Rating"])["UserID"].agg(pv="size")
    log.info("df_group: \n{}".format(df_group.head()))
    # 对于这样的数据, 我想查看按月份, 不同评分的次数趋势, 无法实现. 因为没有另一个轴
    # 案例: 每个月当中, 评分的数量.
    # 方式一. 将二维索引变成行列式
    df_unstack = df_group.unstack()
    log.info("df_group unstack: \n{}".format(df_unstack.head()))
    log.info("df_group plot: \n{}".format(df_unstack.plot()))
    # 方式二. 将索引变成普通列,自行定义x/y轴
    df_reset = df_group.reset_index()
    log.info("df_reset: \n{}".format(df_reset.head()))
    # pivot 是 pandas 中的一个数据重塑函数, 用于将数据从"长"格式转换为"宽"格式, 它可以将某些行值转换为列标题,从而使数据更易于比较和分析
    # pivot 这个单词的原意是"支点","枢轴", 在数据分析中,pivot 操作就像是将数据绕着某个轴进行旋转或转换,从"长"格式变成"宽"格式
    df_reset = df_reset.pivot(index="pdate", columns="Rating", values="pv")
    log.info("df_reset pivot: \n{}".format(df_reset))
    # plot 是 pandas 中的一个数据可视化函数, 用于将数据绘制成图表
    # plot 这个单词的原意是"绘图","作图"
    log.info("df_reset plot: \n{}".format(df_reset.plot()))
    plt.show(block=True)
