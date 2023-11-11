from sqlalchemy import create_engine, text

from pandas_demo import log, pd

if __name__ == '__main__':
    df = pd.read_excel("C:/WorkSpace/python3-example/material/学生信息表.xlsx")
    log.info("df: \n{}".format(df.head()))
    log.info("df index name: {}".format(df.index.name))
    # 定义索引的名称
    df.index.name = "id"
    log.info("df: \n{}".format(df.head()))
    log.info("df index name: {}".format(df.index.name))
    engine = create_engine("mysql+pymysql://root:By96o122@localhost:3306/springboot")
    connect = engine.connect()
    # 方法1: 当数据表不存在时, 每次覆盖整个表
    df.to_sql(name="student", con=engine, if_exists="replace")
    log.info("show create: \n{}".format(connect.execute(text("show create table student")).first()[1]))
    log.info("count: \n{}".format(connect.execute(text("select count(1) from student")).first()))
    log.info("select: \n{}".format(connect.execute(text("select * from student limit 3")).first()))
    # 方法2: 当数据表存在时, 每次新增数据
    df_new = df.loc[:4, :]
    df_new.to_sql(name="student", con=engine, if_exists="append")
    log.info("fetchall: \n{}".format(connect.execute(text("select * from student where id < 2")).fetchall()))
