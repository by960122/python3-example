# 特征最影响结果的K个特征
from sklearn.feature_selection import SelectKBest
# 卡方检验, 作为SelectKBest的参数
from sklearn.feature_selection import chi2

from example.pandas_demo import log, pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/titanic_train.csv"
    df = pd.read_csv(file_path)
    # 案例: 泰坦尼克沉船事件中, 最影响生死的因素有哪些?
    df = df[["PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].copy()
    log.info("df: \n{}".format(df.head()))
    # 数据预处理
    # 1. age 填充平均值
    df["Age"] = df["Age"].fillna(df["Age"].median())
    # 2. 将性别换成数字
    df.loc[df["Sex"] == "male", "Sex"] = 0
    df.loc[df["Sex"] == "female", "Sex"] = 1
    # 3. 给Embarked列填充空值, 字符串转为数字
    df["Embarked"] = df["Embarked"].fillna(0)
    df.loc[df["Embarked"] == "S", "Embarked"] = 1
    df.loc[df["Embarked"] == "C", "Embarked"] = 2
    df.loc[df["Embarked"] == "Q", "Embarked"] = 3
    # 4. 将特征列和结果列拆开
    df_feature = df.pop("Survived")
    df_result = df
    # 5. 使用卡方检验选择topK的特征
    best_features = SelectKBest(score_func=chi2, k=len(df_result.columns))
    # 选择所有的特征, 目的是看到特征重要性排序
    fit = best_features.fit(df_result, df_feature)
    # 6. 按照重要性顺序打印特征列表
    df_scores = pd.DataFrame(fit.scores_)
    log.info("df_scores: \n{}".format(df_scores.head()))
    df_columns = pd.DataFrame(df_result.columns)
    log.info("df_columns: \n{}".format(df_columns.head()))
    # 合并2个df
    df_feature_scores = pd.concat([df_columns, df_scores], axis=1)
    # 列名
    df_feature_scores.columns = ["feature_name", "score"]
    df_feature_scores.sort_values(by="score", ascending=False, inplace=True)
    log.info("df_feature_scores: \n{}".format(df_feature_scores.head()))
