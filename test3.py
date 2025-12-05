## Count how many cars have at least one recorded speed above a certain threshold: 60 km/h

import pandas as pd

df = pd.read_csv("car_dataset.csv")

df_above = df[df["speed"] > 60]
print(df_above)

number_unique_cars = df_above["car_id"].nunique()

print(f"Number of cars with at least one speed above 60 km/h: {number_unique_cars}")