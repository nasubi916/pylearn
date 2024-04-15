import pandas as pd

df_data = pd.read_csv("./outputEditBoosted4MantineChart.csv")

#json形式で出力する
df_data.to_json("./data_pd.json", orient="records")