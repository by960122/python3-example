from sklearn.linear_model import LogisticRegression

from example.pandas_demo import log, pd

if __name__ == '__main__':
    # Pandas的 get_dummies 用于机器学习的特征处理
    # 普通分类: 性别, 颜色
    # 顺序分类: 评分, 级别
    # 对于评分,可以把这个分类直接转换成1、2、3、4、5表示,因为它们之间有顺序、大小关系
    # 但是对于颜色这种分类,直接用1/2/3/4/5/6/7表达,是不合适的,因为机器学习会误以为这些数字之间有大小关系
    # get_dumrMies就是用于颜色、性别这种特征的处理,也叫作one-hot-encoding处理
    # 比如: 
    # 男性: 1 0
    # 女性: 0 1
    # 这就叫做one-hot-encoding, 是机器学习对类别的特征处理
    file_path = "C:/WorkSpace/python3-example/material/titanic_train.csv"
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', None)
    log.info("df: \n{}".format(df.head()))
    df.info()
    # 数值特征: Fare
    # 分类-有序特征: Age
    # 可以用数字的方法处理, 使用平均值填充控制
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    # RangeIndex: 30 entries, 这里的30 等于 列里边的数字, 就说明没有空值
    df.info()
    # 删除不要的特征
    df.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)
    # 分类-普通特征: PassengerId, Pclass, Sex, SibSp, Parch, Embarked
    # 单列
    # df = pd.get_dummies(df["Sex"])
    # 注意,One-hot-Encoding 一般要去掉一列,不然会出现 dummy variable trap 因为一个人不是male就是femal,它俩有推导关系
    df_feature = pd.get_dummies(df,
                                # 要转码的列
                                columns=["Pclass", "Sex", "SibSp", "Parch", "Embarked"],
                                # 生成的列名前缀
                                prefix=["Pclass", "Sex", "SibSp", "Parch", "Embarked"],
                                # 把空值也做编码
                                dummy_na=True,
                                # 把 1 of k 移除(dummy variable trap)
                                drop_first=True)
    log.info("df_feature: \n{}".format(df_feature.head()))
    # Survived 为要预测的 Label
    # 取出某一列
    df_survived = df_feature.pop("Survived")
    log.info("df_survived: \n{}".format(df_survived.head()))
    regression = LogisticRegression(solver="liblinear")
    regression.fit(df_feature, df_survived)
    # 准确率
    log.info("score: {}".format(regression.score(df_feature, df_survived)))
