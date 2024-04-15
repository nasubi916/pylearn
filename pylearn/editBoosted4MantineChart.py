import pandas as pd


# ファイル読み込み
df = pd.read_csv("editBoosted.csv")

# 列名の変更
df.columns = ["Project_name", "date", "duration"]

# 日付を年月のみの形式に変換
df["date"] = pd.to_datetime(df["date"])
df["year_month"] = df["date"].dt.strftime("%Y-%m")

# 時間を秒に変換 小数点以下を切り捨て durationは削除しない
df["duration_second"] = pd.to_timedelta(df["duration"]).dt.total_seconds().astype(int)


# プロジェクト名と年月でグループ化し、時間を集計
df = df.groupby(["Project_name", "year_month"])["duration_second"].sum().reset_index()


df = df[["year_month", "Project_name", "duration_second"]]


# year_monthでまとめて､Project_nameの行をカラムにする
df = df.pivot(index="year_month", columns="Project_name", values="duration_second").reset_index()

# 数値がない場合は0を代入
df = df.fillna(0)

# コラム1以外はセルで小数点以下を切り捨て
for col in df.columns[1:]:
    df[col] = df[col].astype(int)

# 集計結果をCSVファイルに出力
df.to_csv("outputEditBoosted4MantineChart.csv", index=False)


#! 外部化したい
df_data = pd.read_csv("./outputEditBoosted4MantineChart.csv")
#json形式で出力する
df_data.to_json("./outputEditBoosted4MantineChart.json", orient="records")