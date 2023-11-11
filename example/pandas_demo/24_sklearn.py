from sklearn.linear_model import LogisticRegression

from example.pandas_demo import log, pd

regression = LogisticRegression

if __name__ == '__main__':
    # 机器学习 sklearn 已经替换成 scikit-learn, 安装的时候请注意
    file_path = "C:/WorkSpace/python3-example/material/titanic_train.csv"
    df = pd.read_csv(file_path)
    log.info("df: \n{}".format(df.head()))
    # 1. 只挑选2列作为预测需要的特征
    feature_cols = ["Pclass", "Parch"]
    df_feature = df.loc[:, feature_cols]
    log.info("df_feature: \n{}".format(df_feature.head()))
    # 2. 单独提取 是否存活 的列, 作为预测目标
    # 另一种写法: df_survived = df.Survived
    df_survived = df["Survived"]
    log.info("df_survived: \n{}".format(df_survived.head()))
    # 3. 训练模型
    regression = LogisticRegression()
    regression.fit(df_feature, df_survived)
    # 4. 对于未知数据使用模型
    log.info("drop duplicates: \n{}".format(df_feature.drop_duplicates().sort_values(by=["Pclass", "Parch"])))
    # 预测结果, 不建议直接使用 [[2,4]], 会有告警说没有指定特征名称
    df_prob = pd.DataFrame([[2, 4]], columns=["Pclass", "Parch"])
    log.info("predict: {}".format(regression.predict(df_prob)))
    # 预测存活率
    log.info("predict: {}".format(regression.predict_proba(df_prob)))
