# ライブラリのインポート
import pandas as pd
import seaborn as sbn
import numpy as np
import matplotlib.pyplot as plt

# やりたいこと→boostedのデータからどの時間帯が一番{タグの名前}をやっているかを調べる
# 最頻値の出力 毎日の記録したデータの重なりを可視化する

# 始めた時間が一番多い時間帯を出力する

# csvデータのインポート
df = pd.read_csv("assets/boosted.csv")

df.columns = [
    "Project name",
    "Task name",
    "Date",
    "Start time",
    "End time",
    "Duration",
    "Time zone",
    "Project archived",
    "Task completed",
]

print(df[["Project name","Duration","Date"]])

editDf = df[["Project name","Duration","Date"]]

#Date をMonthだけにしてDurationを合計する
editDf["Date"] = pd.to_datetime(df["Date"])
editDf["Month"] = editDf["Date"].dt.strftime("%Y-%m")
editDf["Duration"] = pd.to_datetime(editDf["Duration"])

#HH:mm:ssを秒数に変換
editDf["Duration"] = editDf["Duration"].dt.hour * 3600 + editDf["Duration"].dt.minute * 60 + editDf["Duration"].dt.second

#月ごとの合計時間を求める
editDf["MonthlySum"] = editDf.groupby("Month")["Duration"].transform("sum")

print(editDf[["Project name","Duration","Date","Month","MonthlySum"]])

project_name = df["Project name"].to_numpy()

# start time hourのsort
plt.legend(loc="upper left")

# ヒートマップを作成
