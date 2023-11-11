import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def read_date():
    return pd.read_csv(filepath_or_buffer="C:/WorkSpace/python3-example/material/users.dat",
                       sep=":",
                       engine="python",
                       names="UserID:Gender:Age:Occupation:Zip-core".split(":"))


@app.route('/users')
def get_users():
    df = read_date()
    df_male = df[df["Gender"] == "M"].head()
    df_female = df[df["Gender"] == "F"].head()
    return render_template("users.html", male_data=df_male.to_html(classes="male", index=False),
                           female_data=df_female.to_html(classes="female", index=False))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
