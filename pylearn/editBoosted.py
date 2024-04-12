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

# year_monthの昇順､Project_nameの昇順でソート
df = df.sort_values(["year_month", "Project_name"], ascending=[True, True])


#! 時間をHH:MM:SSに変換関数 外部化したい
def format_timedelta(timedelta):
  total_sec = timedelta.total_seconds()
  # hours
  hours = total_sec // 3600
  # remaining seconds
  remain = total_sec - (hours * 3600)
  # minutes
  minutes = remain // 60
  # remaining seconds
  seconds = remain - (minutes * 60)
  # total time
  return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

# duration HH:MM:SSに変換
df["duration"] = pd.to_timedelta(df["duration_second"], unit="s").apply(format_timedelta)

df = df[[ "year_month","Project_name", "duration_second","duration"]]

# 集計結果をCSVファイルに出力
df.to_csv("outputEditBoosted.csv")