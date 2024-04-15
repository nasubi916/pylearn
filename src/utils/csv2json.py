import pandas as pd

def csc2json() :
  df_data = pd.read_csv("./outputEditBoosted4MantineChart.csv")
  #json形式で出力する
  return df_data.to_json("./data_pd.json", orient="records")