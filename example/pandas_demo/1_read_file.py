from sqlalchemy import create_engine

from pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/ratings.csv"
    # pd.read_csv
    # pd.read_excel
    # pd.read_sql
    ratings = pd.read_csv(file_path)
    #  查看前几行数据
    log.info("head1: \n{}".format(ratings.head(1)))
    # 查看数据的形状
    log.info("shape: {}".format(ratings.shape))
    # 查看列名
    log.info("columns: {}".format(ratings.columns))
    # 查看索引列
    log.info("index: {}".format(ratings.index))
    # 查看每列的数据类型
    log.info("dtypes: \n{}".format(ratings.dtypes))

    file_path = "C:/WorkSpace/python3-example/material/access_pvuv.txt"
    pvuv = pd.read_csv(file_path, sep=" ", header=None, names=['pdate', 'pv', 'uv'])
    log.info("head2: \n{}".format(pvuv.head(3)))
    file_path = "C:/WorkSpace/python3-example/material/access_pvuv.xlsx"
    # 需要安装 openpyxl
    excel = pd.read_excel(file_path)
    log.info("head3: \n{}".format(excel.head(2)))
    # 直接用pymysql有告警: pandas only supports SQLAlchemy...
    # connect = pymysql.connect(host='127.0.0.1', user="root", passwd="By96o122", database="springboot", charset="utf8")
    engine = create_engine("mysql+pymysql://root:By96o122@localhost:3306/springboot")
    mysql = pd.read_sql("select * from shedlock", con=engine)
    log.info("mysql: \n{}".format(mysql.head()))
