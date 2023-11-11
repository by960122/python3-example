from pyecharts import options as opts
from pyecharts.charts import Line

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # Echarts是百度开源的非常好用强大的可视化图表库,Pyecharts是它的Python库版本
    # 案例见 31_*
    file_path = "C:/WorkSpace/python3-example/material/baidu_stocks.xlsx"
    df = pd.read_excel(file_path, index_col="datetime", parse_dates=True)
    log.info("df: \n{}".format(df.head()))
    log.info("index: \n{}".format(df.index))
    df.sort_index(inplace=True)
    log.info("df: \n{}".format(df.head()))

    line = Line()
    # x 轴
    line.add_xaxis(df.index.to_list())
    # 每个 y 轴
    line.add_yaxis("开盘价", df["open"].round(2).tolist())
    line.add_yaxis("收盘价", df["close"].round(2).tolist())
    # tooltip_opts 在图表中展示 十字标
    line.set_global_opts(title_opts=opts.TitleOpts(title="百度股票-2019年"),
                         tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"))
    # 渲染数据
    # line.render("./aaa.html")
