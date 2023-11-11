from pyecharts import options as opts
from pyecharts.charts import Line, Bar, Pie

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # 分析日志
    file_path = "C:/WorkSpace/python3-example/material/log.txt"
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(file_path, sep=" ", header=None)
    log.info("df: \n{}".format(df.head()))
    df = df[[0, 3, 6, 9]].copy()
    df.columns = ["ip", "stime", "state", "client"]
    # 1. 统计 spider 的比例
    df["is_spider"] = df["client"].str.lower().str.contains("spider")
    df_spider = df["is_spider"].value_counts()
    log.info("df: \n{}".format(df.head()))
    log.info("df_spider: \n{}".format(df_spider.head()))
    bar = (Bar().add_xaxis([str(x) for x in df_spider.index])
           .add_yaxis("是否为Spider", df_spider.values.tolist())
           .set_global_opts(title_opts=opts.TitleOpts(title="爬虫访问量占比")))
    # bar.render("./bar.html")
    # 2. 访问状态码的数量对比
    df_state = df.groupby("state").size()
    log.info("df_state: \n{}".format(df_state.head()))
    pie = (Pie().add("状态码比例", list(zip(df_state.index, df_state))).set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    # pie.render("./pie.html")
    # 3. 实现按小时, 按天力度的流量统计
    df["stime"] = pd.to_datetime(df["stime"].str[1::], format="%d/%b/%Y:%H:%M:%S")
    df.set_index("stime", inplace=True)
    ## 按小时统计
    df_puuv = df.resample("h")["ip"].agg(pv="size", uv="unique")
    # df_puuv = df.resample("6h")["ip"].agg(pv="size", uv="unique")
    # df_puuv = df.resample("D")["ip"].agg(pv="size", uv="unique")
    log.info("df_puuv: \n{}".format(df_puuv.head()))
    line = (Line()
            .add_xaxis(df_puuv.index.to_list()).add_yaxis("PV", df_puuv["pv"].to_list())
            .add_yaxis("UV", df_puuv["uv"].to_list())
            .set_global_opts(title_opts=opts.TitleOpts(title="PVUV数据对比"),
                             tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")))
    # line.render("./line.html")
