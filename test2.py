## Given the same dataset with columns: car_id, timestamp, speed, calculate the variance of speed for each car and return the top 3 cars with
## the highest speed variance

import pandas as pd

df = pd.read_csv("car_dataset.csv")

df_grouped = df.groupby("car_id")["speed"]
df_var = df_grouped.var().reset_index()
top3cars = df_var.sort_values(by="speed", ascending=True)

print(top3cars)
