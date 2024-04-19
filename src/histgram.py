# ライブラリのインポート
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

# やりたいこと→boostedのデータからどの時間帯が一番{タグの名前}をやっているかを調べる
# 最頻値の出力 毎日の記録したデータの重なりを可視化する

# 始めた時間が一番多い時間帯を出力する


# input
print("input file tags name(exa : all,program,read,write,game,anime,movie,study)")
tags = input()

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

#! タグの大文字小文字を無視させたい (df["Project name"].strにcasefold()を使いたい)
# タグの名前と一致する行を取り出す
match tags:
    case "program":
        df = df[df["Project name"].str.contains(tags)]
    case "read":
        df = df[df["Project name"].str.contains(tags)]
    case "write":
        df = df[df["Project name"].str.contains(tags)]
    case "game":
        df = df[df["Project name"].str.contains(tags)]
    case "anime":
        df = df[df["Project name"].str.contains(tags.casefold())]
    case "movie":
        df = df[df["Project name"].str.contains(tags.casefold())]
    case "study":
        df = df[df["Project name"].str.contains(tags.casefold())]
    case _:
        pass

# start timeが00:00:00のデータを削除
df = df[df["Start time"] != "0:00:00"]

# end timeが23:59:59のデータを削除
df = df[df["End time"] != "23:59:59"]

# hourを取り出す 2:34:12 -> 2
df["Start time hour"] = df["Start time"].str.extract(r"(\d+):")
df["End time hour"] = df["End time"].str.extract(r"(\d+):")

print(df[["Start time hour", "End time hour"]])

# start time hourのsort
df["End time hour"] = df["End time hour"].astype(int)
df["Start time hour"] = df["Start time hour"].astype(int)
plt.legend(loc="upper left")

# ヒストグラムを0~24時間で表示
plt.hist(df["Start time hour"], bins=24, range=(0, 24), alpha=0.5, label="Start time")
plt.hist(df["End time hour"], bins=24, range=(0, 24), alpha=0.5, label="End time")

# 0~24時間だけを表示できなかった ↓で解決
plt.xlim(0, 24)

plt.ylabel("count")
plt.xlabel("hour")
plt.xticks(range(0, 24,3))
plt.title(tags + " start end histogram")
plt.legend()
plt.show()


# ヒストグラムを0~24時間で表示

mode_index = df["Start time hour"].argmax()
