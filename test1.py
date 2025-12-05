## Given a dataset with columns car_id, timestamp, speed, write Python code to compute the average speed car per car
## and return the top 5 cars with the highest average speed

import pandas as pd

df = pd.read_csv("car_dataset.csv")

average_speed = df.groupby("car_id")["speed"].mean()

average_speed_sorted = average_speed.sort_values(ascending=False)

print("These are the top 5 cars with the highest average speed:")
for i in range(5):
    print(f"{i+1}º - {average_speed_sorted.iloc[i]:.2f}")

## How would you do this in SQL?

# In SQL, to calculate the average speed per car and return the top 5 cars with the highest average speed, the query would be:
# SELECT car_id, AVG(speed) AS average_speed
# FROM my_table
# GROUP BY car_id
# ORDER BY average_speed DESC
# LIMIT 5;

## How would you do this on Spark for 100M rows?

# import SparkSession from PySpark library, import avg from PySpark library

# spark = SparkSession.builder.appName("CarAnalysis").getOrCreate()
# df = spark.read_csv("car_dataset.csv", header=True, inferSchema=True)
# top_5_cars = df.groupBy("car_id").agg(avg("speed").alias("average_speed")) \ .orderBy("average_speed", ascending=False) \ .limit(5)