from example.pandas_demo import pd

if __name__ == '__main__':
    file_path = "C:/WorkSpace/python3-example/material/titanic_train.csv"
    df = pd.read_csv(file_path)
    # 1. select ** from ** limit
    df[["PassengerId", "Survived"]].head(2)
    # 2. select ** from ** where
    condition = (df["Sex"] == "male") & (df["Age"] >= 20.0) & (df["Age"] <= 40.0)
    df[condition].head(2)
    # 3. in 和 not in
    df[df["Pclass"].isin((1, 2))].head()
    df[~df["Pclass"].isin((1, 2))].head()
    # 4. groupby
    df.groupby("Sex").aggregate({"Survived": "sum", "Age": "mean", "Fare": "mean"})
    # 5. 多个列聚合
    df.groupby(["Survived", "Sex"]).aggregate({"Age": "mean", "Fare": "mean"})
    # 6. join: 见 12_merge.py
    # 7. union 见 13_concat.py
    # 8. order limit
    df.sort_values("Fare", ascending=False).head()
    # 9. group top n
    df.groupby(["Survived", "Sex"]).apply(lambda df: df.sort_values("Age", ascending=False).head(2),
                                          include_groups=False)
    # 10. update
    df[condition] = 0
    # 11. delete
    df_new = df[df["Age"] != 0]
